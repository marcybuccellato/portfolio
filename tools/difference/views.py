import json
import math

from django.http import JsonResponse
from django.views.generic import FormView

from difference.forms import DifferenceForm
from difference.models import Difference

class DifferenceView(FormView):
    """
    Allows user to query on a number and see the difference between the sum of 
    the squares of the first n natural numbers and the square of the sum of the 
    same first n natural numbers, where n is guaranteed to be no greater than 
    100.
    """
    form_class = DifferenceForm
    # TODO: Use proper form handling with validation.

    # TODO: Move this method to the model and autoset the difference value upon
    # saving.
    def get_difference(self, number):
        """
        Get difference between the sum of the squares and the square of the sums
        for a given number
        """
        if number > 100:
            raise ValueError('Number must be less than 100')

        sum_of_the_squares = 0
        sum_of_the_numbers = 0
        for x in range(1, number + 1):
            sum_of_the_squares += math.pow(x, 2)
            sum_of_the_numbers += x

        square_of_the_sums = math.pow(sum_of_the_numbers, 2)

        return square_of_the_sums - sum_of_the_squares

    def get_context_data(self, **kwargs):
        context = {}
        number = self.request.GET.get('number')
        if number:
            number = int(number)
            # TODO: Add error handling to ensure 'number' is numerical.

            difference, created = Difference.objects.get_or_create(number=number)
            if created:
                difference.value = self.get_difference(number)

            difference.occurrences = difference.occurrences + 1
            difference.save()

            context = {
                "datetime": difference.update_dt,
                "value": difference.value,
                "number": difference.number,
                "occurrences": difference.occurrences
            }

        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)