# -*- coding: utf-8 -*-

import scrapy


class IrnaItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    attr = scrapy.Field()


class IrnaSpider(scrapy.Spider):
    name = 'irna'
    allowed_domains = ['irna.ir']
    start_urls = ["http://irna.ir/",
                  "http://irna.ir/firstpage.aspx",
                  "http://irna.ir/fa/services/5/سیاسی",
                  "http://irna.ir/fa/services/6/سیاسی/رهبر_انقلاب",
                  "http://irna.ir/fa/services/7/سیاسی/دولت",
                  "http://irna.ir/fa/services/8/سیاسی/مجلس",
                  "http://irna.ir/fa/services/11/سیاسی/سیاست_خارجی_و_هسته ای",
                  "http://irna.ir/fa/services/13/سیاسی/احزاب _و_تشکل_ها",
                  "http://irna.ir/fa/services/89/سیاسی/سایر",
                  "http://irna.ir/fa/services/20/اقتصادی",
                  "http://irna.ir/fa/services/27/اقتصادی/اقتصاد_کلان",
                  "http://irna.ir/fa/services/21/اقتصادی/انرژی",
                  "http://irna.ir/fa/services/26/اقتصادی/بانک_-_بیمه_-_بورس",
                  "http://irna.ir/fa/services/25/اقتصادی/امور_زیر_بنایی",
                  "http://irna.ir/fa/services/23/اقتصادی/صنعت_و_معدن",
                  "http://irna.ir/fa/services/24/اقتصادی/کشاورزی",
                  "http://irna.ir/fa/services/22/اقتصادی/تجارت",
                  "http://irna.ir/fa/services/207/اقتصادی/اشتغال-تعاون",
                  "http://irna.ir/fa/services/85/اقتصادی/سایر",
                  "http://irna.ir/fa/services/32/اجتماعی",
                  "http://irna.ir/fa/services/33/اجتماعی/بهداشت_رفاه",
                  "http://irna.ir/fa/services/34/اجتماعی/حقوقی_-_قضایی",
                  "http://irna.ir/fa/services/38/اجتماعی/زن_و_خانواده",
                  "http://irna.ir/fa/services/39/اجتماعی/اشتغال_و_رفاه",
                  "http://irna.ir/fa/services/35/اجتماعی/انتظامی_-_حوادث",
                  "http://irna.ir/fa/services/9/اجتماعی/دفاعی_و_انتظامی",
                  "http://irna.ir/fa/services/196/اجتماعی/دفاع_مقدس",
                  "http://irna.ir/fa/services/87/اجتماعی/سایر",
                  "http://irna.ir/fa/services/41/فرهنگی",
                  "http://irna.ir/fa/services/47/فرهنگی/میراث_فرهنگی_و_گردشگری",
                  "http://irna.ir/fa/services/44/فرهنگی/سینما_-_تئاتر_-_تلویزیون",
                  "http://irna.ir/fa/services/43/فرهنگی/فرهنگ_و_ادب",
                  "http://irna.ir/fa/services/46/فرهنگی/آموزش",
                  "http://irna.ir/fa/services/45/فرهنگی/موسیقی",
                  "http://irna.ir/fa/services/216/فرهنگی/تجسمی",
                  "http://irna.ir/fa/services/42/فرهنگی/معارف",
                  "http://irna.ir/fa/services/129/فرهنگی/رسانه",
                  "http://irna.ir/fa/services/211/فرهنگی/دانشگاه",
                  "http://irna.ir/fa/services/88/فرهنگی/سایر",
                  "http://irna.ir/fa/services/180/علمی",
                  "http://irna.ir/fa/services/40/علمی/محیط زیست",
                  "http://irna.ir/fa/services/143/علمی/فنآوری",
                  "http://irna.ir/fa/services/141/علمی/علوم",
                  "http://irna.ir/fa/services/180/علمی/جامعه_اطلاعاتی",
                  "http://irna.ir/fa/services/142/علمی/پزشکی",
                  "http://irna.ir/fa/services/14/ورزشی",
                  "http://irna.ir/fa/services/15/ورزشی/فوتبال_و_فوتسال",
                  "http://irna.ir/fa/services/18/ورزشی/توپ_و_تور",
                  "http://irna.ir/fa/services/16/ورزشی/کشتی_و_وزنه_برداری",
                  "http://irna.ir/fa/services/19/ورزشی/ورزشهای_پایه",
                  "http://irna.ir/fa/services/17/ورزشی/ورزشهای_رزمی",
                  "http://irna.ir/fa/services/195/ورزشی/ورزشهای_راکتی",
                  "http://irna.ir/fa/services/173/ورزشی/ورزش_بانوان",
                  "http://irna.ir/fa/services/84/ورزشی/نهادها_و_سایر_رشته_ها",
                  "http://irna.ir/fa/services/90/ورزشی/دانش_ورزش",
                  "http://irna.ir/fa/services/178/ورزشی/خارجی",
                  "http://irna.ir/fa/services/1/خارجی",
                  "http://irna.ir/fa/services/193/خارجی/آمریکا",
                  "http://irna.ir/fa/services/194/خارجی/آفریقا",
                  "http://irna.ir/fa/services/2/خارجی/اروپا",
                  "http://irna.ir/fa/services/3/خارجی/آسیا_و_اقیانوسیه",
                  "http://irna.ir/fa/services/4/خارجی/خاورمیانه",
                  "http://irna.ir/fa/services/82/خارجی/روابط_خارجی",
                  "http://irna.ir/fa/services/54/استانها",
                  "http://irna.ir/fa/services/56/استانها/آذربایجان_شرقی",
                  "http://irna.ir/fa/services/57/استانها/آذربایجان_غربی",
                  "http://irna.ir/fa/services/58/استانها/اردبیل",
                  "http://irna.ir/fa/services/59/استانها/اصفهان",
                  "http://irna.ir/fa/services/60/استانها/ایلام",
                  "http://irna.ir/fa/services/61/استانها/تهران",
                  "http://irna.ir/fa/services/62/استانها/خراسان_شمالی",
                  "http://irna.ir/fa/services/63/استانها/خوزستان",
                  "http://irna.ir/fa/services/64/استانها/زنجان",
                  "http://irna.ir/fa/services/65/استانها/سمنان",
                  "http://irna.ir/fa/services/66/استانها/فارس",
                  "http://irna.ir/fa/services/67/استانها/سیستان_و_بلوچستان",
                  "http://irna.ir/fa/services/68/استانها/قزوین",
                  "http://irna.ir/fa/services/69/استانها/کردستان",
                  "http://irna.ir/fa/services/70/استانها/کرمان",
                  "http://irna.ir/fa/services/71/استانها/کرمانشاه",
                  "http://irna.ir/fa/services/72/استانها/گلستان",
                  "http://irna.ir/fa/services/73/استانها/گیلان",
                  "http://irna.ir/fa/services/74/استانها/لرستان",
                  "http://irna.ir/fa/services/75/استانها/مازندران",
                  "http://irna.ir/fa/services/76/استانها/مرکزی",
                  "http://irna.ir/fa/services/77/استانها/هرمزگان",
                  "http://irna.ir/fa/services/78/استانها/همدان",
                  "http://irna.ir/fa/services/79/استانها/یزد",
                  "http://irna.ir/fa/services/80/استانها/بوشهر",
                  "http://irna.ir/fa/services/81/استانها/چهارمحال_و_بختیاری",
                  "http://irna.ir/fa/services/91/استانها/قم",
                  "http://irna.ir/fa/services/92/استانها/خراسان_رضوی",
                  "http://irna.ir/fa/services/93/استانها/خراسان_جنوبی",
                  "http://irna.ir/fa/services/94/استانها/کهگیلویه_و_بویراحمد",
                  "http://irna.ir/fa/services/176/استانها/البرز",
                  "http://irna.ir/fa/services/56/استانها/سیاسی",
                  "http://irna.ir/fa/services/57/استانها/اقتصادی",
                  "http://irna.ir/fa/services/58/استانها/اجتماعی",
                  "http://irna.ir/fa/services/59/استانها/فرهنگی",
                  "http://irna.ir/fa/services/60/استانها/ورزشی",
                  "http://irna.ir/fa/services/61/استانها/علمی",
                  "http://irna.ir/fa/services/62/استانها/سایر",
                  "http://irna.ir/fa/services/103/پژوهش",
                  "http://irna.ir/fa/services/104/پژوهشهای_خبری/پژوهشهای_اجتماعی_فرهنگی",
                  "http://irna.ir/fa/services/105/پژوهشهای_خبری/پژوهشهای_اقتصادی",
                  "http://irna.ir/fa/services/106/پژوهشهای_خبری/پژوهشهای_سیاسی",
                  "http://irna.ir/fa/services/107/پژوهشهای_خبری/پژوهشهای_بین_المللی",
                  "http://irna.ir/fa/services/108/پژوهشهای_خبری/نظرسنجی",
                  "http://irna.ir/fa/services/109/پژوهشهای_خبری/نشریات_پژوهشی",
                  "http://irna.ir/fa/services/110/پژوهشهای_خبری/پژوهشهای_استانی",
                  "http://irna.ir/fa/services/111/پژوهشهای_خبری/سایر",
                  "http://irna.ir/fa/services/212/حوادث",
                  "http://irna.ir",
                  "http://irna.ir/fa/51/عکس",
                  "http://irna.ir/fa/203/عکس/خارجی",
                  "http://irna.ir/fa/204/عکس/استانی",
                  "http://irna.irhttp://film.irna.ir/",
                  "http://irna.ir/fa/page/225/فیلم-و-صدا",
                  "http://irna.ir/fa/advancedsearch.aspx",
                  "http://irna.ir/fa/links.aspx?cid=2",
                  "http://irna.ir/fa/services/1000525/مناسبت_های_خبری/فجر/بیست_و_پنجمین_نمایشگاه_بین_المللی_کتاب",
                  "http://irna.ir/fa/services/1000539/مناسبت_های_خبری/سفیر_فطرت_ها_(_سفر_رییس_جمهور_به_نیویورک_)",
                  "http://irna.ir/fa/services/1000508/مناسبت_های_خبری/فجر/نهمین_دوره_انتخابات_مجلس_شورای_اسلامی",
                  "http://irna.ir/fa/services/1000117/مناسبت_های_خبری/کارنامه_سفرهای_استانی_دولت",
                  "http://irna.ir/fa/services/1000115/مناسبت_های_خبری/گردشگری",
                  "http://irna.ir/fa/services/1000520/مناسبت_های_خبری/فجر",
                  "http://irna.ir/fa/services/1000519/مناسبت_های_خبری/جشنواره_های_هنری_فجر",
                  "http://irna.ir/fa/services/1000514/مناسبت_های_خبری/جهانی_شدن",
                  "http://irna.ir/fa/services/1000512/مناسبت_های_خبری/انقلاب_های_مردمی_و_بیداری_اسلامی",
                  "http://irna.ir/fa/services/1000114/مناسبت_های_خبری/خصوصی_سازی",
                  "http://irna.ir/fa/services/1000518/مناسبت_های_خبری/سفر_رئیس_جمهور_به_آمریکای_لاتین",
                  "http://irna.ir/fa/services/1000523/مناسبت_های_خبری/سال_تولید_ملی__حمایت_از_کار_و_سرمایه_ملی",
                  "http://irna.ir/fa/services/1000528/مناسبت_های_خبری/بیست_و_سومین_سالگرد_ارتحال_امام_خمینی(ره)",
                  "http://irna.ir/fa/services/1000530/مناسبت_های_خبری/جزیره_ابوموسی",
                  "http://irna.ir/fa/services/531/مناسبت_های_خبری/بیست_و_نهمین_دوره_مسابقات_بین_المللی_قرآن",
                  "http://irna.ir/fa/services/1000531/مناسبت_های_خبری/بیست_و_نهمین_دوره_مسابقات_بین_المللی_قرآن",
                  "http://irna.ir/fa/services/1000526/مناسبت_های_خبری/المپیک_و_پاراالمپیک_لندن_2012",
                  "http://irna.ir/fa/services/1000527/مناسبت_های_خبری/صدمین_سفر_استانی_هیئت_دولت",
                  "http://irna.ir/fa/services/1000130/مناسبت_های_خبری/روز_قدس",
                  "http://irna.ir/fa/services/1000532/مناسبت_های_خبری/شانزدهمین_اجلاس_سران_جنبش_غیر_متعهدها",
                  "http://irna.ir/fa/services/1000582/پرونده_خبری/نشست_92",
                  "http://irna.ir/fa/services/1000590/پرونده_خبری/آخرین_تحولات_عراق",
                  "http://irna.ir/fa/services/1000584/پرونده_خبری/بیانات_رهبری",
                  "http://irna.ir/fa/services/1000576/پرونده_خبری/اقتصاد_مقاومتی",
                  "http://irna.ir",
                  "http://irna.ir/fa/services/1000591/پرونده_خبری/با_شهدا",
                  "http://irna.ir/fa/services/1000609/پرونده_خبری/جام_2015",
                  "http://irna.ir/fa/telex.aspx?area=0",
                  "http://irna.ir/fa/telex.aspx",
                  "http://irna.ir/fa/telex-kind_5.aspx",
                  "http://irna.ir/fa/telex-kind_20.aspx",
                  "http://irna.ir/fa/telex-kind_32.aspx",
                  "http://irna.ir/fa/telex-kind_41.aspx",
                  "http://irna.ir/fa/telex-kind_180.aspx",
                  "http://irna.ir/fa/telex-kind_14.aspx",
                  "http://irna.ir/fa/telex-kind_1.aspx",
                  "http://irna.ir/fa/telex-kind_54.aspx",
                  "http://irna.ir/fa/telex-kind_103.aspx",
                  "http://irna.ir/fa/telex-area_0.aspx",
                  "http://irna.ir/fa/page/242/صفحه-اول-عکس-جدید-ایرنا",
                  "http://irna.ir/fa/page/253/صفحه-لیست-داده-نمای-جدید-ایرنا"]

    def parse(self, response):
        sel = response
        links = sel.xpath('//a/@href').extract()
        for link in links:
            absolute_url = self.start_urls[0] + link
            yield scrapy.Request(absolute_url, callback=self.parse_news)

    def parse_news(self, response):
        item = IrnaItem()
        item["link"] = response.url
        item["attr"] = "".join(
            response.css("#ctl00_ctl00_ContentPlaceHolder_ContentPlaceHolder_NewsContent4_BodyLabel").extract()).encode(
            'utf-8')
        if item["attr"] is None:
            link = item["attr"]
            return link
        else:
            return item
            # if item["attr"] is not None:
            #     return item
            # else:
            #     yield scrapy.Request(item["link"], callback=self.parse)

    # def get_links(self, link):
    #     yield scrapy.Request(link, callback=self.parse)

    def parse_inner_pages(self, link):
        yield scrapy.Request(url=link, callback=self.parse)
