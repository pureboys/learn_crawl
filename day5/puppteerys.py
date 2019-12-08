from pyppeteer import launch
import asyncio
from lxml import etree


async def main():
    bro = await launch(headless=False)
    page = await bro.newPage()
    await page.goto('http://quotes.toscrape.com/', {'waitUntil': 'networkidle2'})

    page_text = await page.content()
    return page_text


def parse(tasked):
    page_text = tasked.result()
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="quote"]')
    for div in div_list:
        content = div.xpath('./span[1]/text()')[0]
        print(content)


task = asyncio.ensure_future(main())
task.add_done_callback(parse)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
