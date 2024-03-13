# prompt/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemplateViewSet, PromptViewSet, InstructionViewSet, RuleViewSet

router = DefaultRouter()
router.register(r'templates', TemplateViewSet)
router.register(r'prompts', PromptViewSet)
router.register(r'instructions', InstructionViewSet)
router.register(r'rules', RuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
