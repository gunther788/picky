#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server import data


def main():
    app = connexion.App(__name__, specification_dir='./swagger/', debug=True)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'picky: Python ICinga2 to KeYbase'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
