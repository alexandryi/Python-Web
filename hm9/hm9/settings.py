BOT_NAME = "hm9"
SPIDER_MODULES = ["hm9.spiders"]
NEWSPIDER_MODULE = "hm9.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "hm9.pipelines.QuotesPipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"
