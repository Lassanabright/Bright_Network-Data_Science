from django.views.generic import TemplateView


class MachineLearningView(TemplateView):
    help="This view is to create a dashboard for supervising the machine learning Project"
    template_name = "data_science/homepage.html"

    def get_context_data(self, **kwargs):
        context = super(MachineLearningView, self).get_context_data(**kwargs)
        context["test"]="test"
        return context
