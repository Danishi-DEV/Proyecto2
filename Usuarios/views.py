from rest_framework.views import APIView
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.conf import settings
from .serializers import ContactSerializer

class SendEmail(APIView):
    
    def post(self, request):
        
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            
            nombres = serializer.validated_data['first_name']
            apellidos = serializer.validated_data['last_name']
            email = serializer.validated_data['email']

            
            page = get_current_site(request)
            mail = 'Confirmación de contacto - Javier Martinez'
            body = render_to_string('emailUser.html',{
                'user': f'{nombres} {apellidos}',
                'email':email,
                'domain':page,
            })
            
            send_mail = EmailMessage(
                mail,body,settings.EMAIL_HOST_USER,to=[email]
            )
            send_mail.content_subtype = 'html'
            send_mail.send()
            
            #correo para el tio
            """emailEmpresa = 'administracion@javieremartinez.co'
            mail2 = f'Correo de {name} {Apellido}'
            body = render_to_string('emailJavier.html',{
                'user':name,
                'email':email,
                'Apellido':Apellido,
                'Telefono':Telefono,
                'Mensaje':Mensaje,
                'domain':page,
            })
            
            send_mail2 = EmailMessage(
                mail2,body,settings.EMAIL_HOST_USER,to=[emailEmpresa]
            )
            send_mail2.content_subtype = 'html'
            send_mail2.from_email = False
            send_mail2.send()"""
            
            return Response({'message': 'Correo enviado exitosamente'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
