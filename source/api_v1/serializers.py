from rest_framework import serializers

from webapp.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        required=False,
    )

    class Meta:
        model = Quote
        fields = ("id", "text", "name", "email", "rating", "status", "created_at")
        read_only_fields = ("id", "created_at", )

    def create(self, validated_data):
        quote = Quote()
        if validated_data['text']:
            quote.text = validated_data["text"]
            quote.email = validated_data["email"]
            quote.name = validated_data["name"]
            quote.save()
            return quote

    def update(self, instance, validated_data):
        if "text" in validated_data.keys():
            instance.text = validated_data['text']
        instance.status = "moderated"
        return instance
