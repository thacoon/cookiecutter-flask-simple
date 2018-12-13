from app import create_app, CONFIG


app = create_app(CONFIG)


if __name__ == '__main__':
    app.run()
