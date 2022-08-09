from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # * suponemos que todo está ok, redireccionamos:
            # enviamos el correo y rediccionamos (configuración de envío de correo)
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", # asunto
                "De {} <{}>\n\nEscribió: \n\n{}".format(name, email, content), # cuerpo
                "no-contestar@inbox.mailtrap.io", # email_origen
                ['django@davidprofe.net'], # email_destino
                reply_to=[email]
            )

            try:
                email.send()
                # Tudo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+'?ok')
            except:
                # algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})