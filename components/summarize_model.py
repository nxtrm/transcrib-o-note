import openai
import json
from flask import Flask

def procedural(api_key):
    #my openai key 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
    app = Flask(__name__)
    openai.api_key = str(api_key)
    @app.route("/", methods=("GET", "POST"))

    def generation():
        question = openai.Completion.create(
        model="text-davinci-003",
        prompt="""generate a coding task in python with a code answer. For example:
        #Task: Create a function that takes in a list of numbers and returns the average of those numbers
        #Answer:
        def average(nums):
            total = 0
            for num in nums:
                total += num
            return total/len(nums)
            """,
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )	
        question = question.choices[0]['text'];return question