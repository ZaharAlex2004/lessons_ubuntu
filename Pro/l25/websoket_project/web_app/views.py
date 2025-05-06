from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from channels.layers import get_channel_layer
from .models import Company
from .forms import CompanyForm
from web_app.ws.consumers import ChatConsumer
from django.http import HttpResponse
from asgiref.sync import async_to_sync


def home_view(request):
    company = Company.objects.first()
    return render(request, 'web_app/chat.html', {'company': company})


def send_notification(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    channel_layer = get_channel_layer()

    channel_layer.group_send(
        f'company_{company.id}',
        {
            'type': 'chat_message',
            'message': f'Company {company.name} details have been updated!'
        }
    )

    return JsonResponse({'status': 'Notification sent'})

def notify_group(request):
    try:
        # Пример запроса к базе данных
        company = Company.objects.first()  # Ищем первую компанию
        if company:
            # Отправляем JSON-ответ
            return JsonResponse({'message': f"Company: {company.name}"})
        else:
            return JsonResponse({'message': "No company found."})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def update_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    company.name = "New Company Name"
    company.save()

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"company_{company_id}",
        {
            "type": "chat_message",
            "message": f"Company {company.name} has been updated."
        }
    )

    return JsonResponse({"status": "success"})


class CompanyUpdateView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)  # Получаем компанию по ID
            return render(request, 'web_app/update_company_form.html', {'company': company})  # Отображаем форму с данными
        except Company.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Company not found'}, status=404)


    def post(self, request, company_id):
        new_name = request.POST.get('name')
        new_location = request.POST.get('location')

        try:

            company = Company.objects.get(id=company_id)
            company.name = new_name
            company.location = new_location
            company.save()

            return JsonResponse({'status': 'success', 'message': 'Company updated successfully'})

        except Company.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Company not found'}, status=404)


def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved, redirecting to 'home'")
            return redirect('home')
    else:
        form = CompanyForm()

    return render(request, 'web_app/create_company.html', {'form': form})
