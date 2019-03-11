from rest_framework import serializers

from event.models import Event, Ticket, Participant
import pyqrcode
import qrtools
import cv2
import zbar
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('name', 'email', 'description', 'cin', 'phone_number', 'birth_date', 'sex', 'is_member', 'ticket')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('number', 'ticket_id', 'qr_code', 'price', 'is_paid')

    def create(self, validated_data):
        request = self.context['request']
        # print(request)
        # print(validated_data)
        qrcode = pyqrcode.create(validated_data['ticket_id'])
        ticket_num = validated_data['ticket_id'][len('tbas'):]
        qrcode.png("qr-code.png", scale=20)

        im = cv2.imread("qr-code.png", cv2.CHAIN_APPROX_SIMPLE)
        image = im # whatever function you use to read an image file into a numpy array
        scanner = zbar.Scanner()
        results = scanner.scan(image)
        for result in results:
            print(result.type, result.data, result.quality, result.position)
            # qr = qrtools.QR()
        # print(qr.decode("qr-code.png"))
        # print(qr.data)
        img = Image.open('qr-code.png', 'r')
        img_w, img_h = img.size
        imgTicket = Image.open('static/img/tickets/ticket_balade_14.png', 'r')
        imgTicket_w, imgTicket_h = imgTicket.size
        width = ((imgTicket_w - img_w) // 2) + 600
        height = ((imgTicket_h - img_h) // 2) + 250
        offset = (width, height)
        imgTicket.paste(img, offset)
        imgTicket.save('out.png')
        print("****")
        imgT = Image.open("out.png")
        print("+++++")
        draw = ImageDraw.Draw(imgT)
        font = ImageFont.truetype("static/fonts/Helvetica-Bold.ttf", 70)
        print("******")
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((width + 250 , height - 30), ticket_num, (0, 0, 0), font=font)
        imgT.save('ticket-'+ticket_num+'.png')
        ticket = Ticket()
        ticket.number = validated_data['number']
        ticket.ticket_id = validated_data['ticket_id']
        ticket.price = validated_data['price']
        ticket.is_paid = validated_data['is_paid']
        ticket.save()
        return ticket


class EventSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)
    participants = ParticipantSerializer(many=True)

    class Meta:
        model = Event
        fields = ('name', 'description', 'start_date', 'end_date', 'tickets', 'participants')
