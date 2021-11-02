#coding:utf-8

from urllib.request import urlopen

def test_render_homepage():
    homepage_html = urlopen("http://localhost:5000").read().decode("utf-8")
    assert "<title>Soh um teste de microservicos</title>" in homepage_html
    assert homepage_html.count("<ul>") >= 2

