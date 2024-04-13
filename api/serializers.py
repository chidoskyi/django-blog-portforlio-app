from rest_framework import serializers
from comment.models import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['reaction_type','user','comment']