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
                    "text": {
                        "skin": 'text',
                        "HTML_ROOT": 'text',
                    }
                }
            },
            files=[("skins/text",
                    ["skins/text/index.txt.tmpl",
                     "skins/text/skin.conf"]),
                   ]
        )
