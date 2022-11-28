import pytermgui as ptg
import config
import pip_cli
import logo

banner = logo.display_message()

OUTPUT = {}

 
def submit(manager: ptg.WindowManager, window: ptg.Window) -> None:
    for widget in window:
        if isinstance(widget, ptg.InputField):
            OUTPUT[widget.prompt] = widget.value
            continue

        if isinstance(widget, ptg.Container):
            label, field = iter(widget)
            OUTPUT[label.value] = field.value

    manager.stop()

with ptg.YamlLoader() as loader:
    loader.load(config.CONFIG)


with ptg.WindowManager() as manager:
    window = (
        ptg.Window(
            "",
            ptg.Container(
                f"{banner}"
            ),
            ptg.Container(
                "",
                ptg.InputField(
                    "", multiline=True
                ),
            ),
            "",
            ["Submit", lambda *_: submit(manager, window)],
            width=60,
            box="DOUBLE",
        )
        .center()
    )

    # For the screenshot's sake
    window.select(0)

    manager.add(window)

#pprint(OUTPUT)