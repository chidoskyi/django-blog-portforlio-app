from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from comment.models import Reaction
from .serializers import ReactionSerializer

# Create your views here.

@api_view(['POST'])
def add_reaction(request):
    serializer = ReactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_reaction(request, reaction_id):
    try:
        reaction = Reaction.objects.get(pk=reaction_id)
    except Reaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    reaction.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def list_reactions(request):
    reactions = Reaction.objects.all()
    serializer = ReactionSerializer(reactions, many=True)
    return Response(serializer.data)

import requests
import json
import random  # Import random module to choose a random reaction type

def create_reaction():
    # Assuming you have obtained user_id, comment_id, reply_id, and post_id from somewhere
    user_id = 1  # Example user ID
    comment_id = 1  # Example comment ID
    reply_id = 1  # Example reply ID
    post_id = 1  # Example post ID

    # Choose a random reaction type from REACTION_CHOICES
    reaction_choices = ['👍', '👎', '❤️', '😲', '😢', '🤣', '😡', '❤️‍🩹', '🤗']
    reaction_type = random.choice(reaction_choices)

    # Define the data to send in the POST request
    data = {
        "reaction_type": reaction_type,
        "user": user_id,
        "comment": comment_id,
        "reply": reply_id,
        "post": post_id
    }

    # Make a POST request to the add_reaction endpoint
    response = requests.post('http://localhost:8000/api/reactions/add/', data=json.dumps(data), headers={'Content-Type': 'application/json'})

    # Check the response
    if response.status_code == 201:
        print("Reaction created successfully")
    else:
        print("Failed to create reaction:", response.json())
        
           
