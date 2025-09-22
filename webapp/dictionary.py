import justpy as jp
from webapp.layout import DefaultLayout
import backend.definition as definition
from webapp import page

class Dictionary(page.Page):

    path = "/dictionary"

    @classmethod
    def serve(cls, req):

        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary!", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        
        output_div = jp.Div(a=div, classes="bg-blue-100 m-2 p-2 text-lg border-2 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type in a word here...",
                 classes="m-2 bg-gray-100 rounded border-2 border-gray-200 w-64 " \
                 "focus:bg-white focus:border-purple-500 py-2 px-4", 
                 outputdiv=output_div)
        input_box.on("input", cls.get_definition)

        # jp.Button(a=input_div, 
        #           text="Get Definition", 
        #           classes="rounded m-2 border-2 border-indigo-200 text-gray-500",
        #           click=cls.get_definition,
        #           outputdiv=output_div,
        #           inputbox=input_box)
        
        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.get(widget.value)
        widget.outputdiv.text = " ".join(defined)