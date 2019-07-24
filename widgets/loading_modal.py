from kivy.uix.modalview import ModalView
from kivy.uix.image import Image


class LoadingModal(ModalView):
    def __init__(self):
        super().__init__(size_hint = (None, None),
                         background_color = (0,0,0,0.3),
                         background = "icons/none-16.png",
                         auto_dismiss = False)
        loading_image = Image(source="icons/loading.zip", anim_delay=0.05,
                              size=(32,32), size_hint=(None, None))
        self.add_widget(loading_image)

