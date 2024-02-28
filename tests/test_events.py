def test_events(page):

    def print_args_start(request):
        print("Request starter: ", request.url)

    def print_args_finish(request):
        print("Request finished: ", request.url)

    page.on("request", print_args_start)
    page.on("requestfinished", print_args_finish)
    page.goto("https://wikipedia.com")
    page.remove_listener("requestfinished", print_args_finish)
