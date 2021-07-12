from weecfg.extension import ExtensionInstaller


def loader():
    return TextInstaller()


class TextInstaller(ExtensionInstaller):
    def __init__(self):
        super(TextInstaller, self).__init__(
            version="0.1",
            name="text",
            description="Plain text skin for weewx",
            author="Vincent Ollivier",
            author_email="v@vinc.cc",
            config={
                "StdReport": {
                    "Text": {
                        "skin": 'Text',
                        "HTML_ROOT": 'text',
                    }
                }
            },
            files=[("skins/Text",
                    ["skins/Text/weather.txt.tmpl",
                     "skins/Text/skin.conf"]),
                   ]
        )
