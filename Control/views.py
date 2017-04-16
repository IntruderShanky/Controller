from django.shortcuts import render
from pykeyboard import PyKeyboard
from rest_framework.response import Response
from rest_framework.views import APIView


class KeyPress(APIView):
    def post(self, request):
        keyboard = PyKeyboard()
        key = request.data["key"]
        if key == "left":
            keyboard.tap_key(keyboard.left_key)
        if key == "right":
            keyboard.tap_key(keyboard.right_key)
        return Response(status=200, data={"success": True, "message": "successfully tapped!"})
