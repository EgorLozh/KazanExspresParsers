import json
import aiohttp
import asyncio
import requests


async def getPage(page, session):
    headers = {
        'authority': 'graphql.kazanexpress.ru',
        'accept': '*/*',
        'accept-language': 'ru',
        'apollographql-client-name': 'web-customers',
        'apollographql-client-version': '1.45.2',
        'authorization': 'Basic a2F6YW5leHByZXNzLWN1c3RvbWVyOmN1c3RvbWVyU2VjcmV0S2V5',
        'baggage': 'sentry-environment=production,sentry-release=kazanexpress%401.45.2,sentry-public_key=84ead3051db54dd6a2ef8f9bc40a9f8b,sentry-trace_id=58a48dff33d948e18f0eef3907dcb2e5',
        'content-type': 'application/json',
        'origin': f'https://kazanexpress.ru/',
        'referer': 'https://kazanexpress.ru/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sentry-trace': '58a48dff33d948e18f0eef3907dcb2e5-88fccc8f50ad81ab-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-iid': 'cb39d276-0fea-45ae-b08f-f9b6224da827',
    }
    json_data = {
        'operationName': 'getMakeSearch',
        'variables': {
            'queryInput': {
                'text': 'мышь',
                'showAdultContent': 'NONE',
                'filters': [],
                'sort': 'BY_RELEVANCE_DESC',
                'pagination': {
                    'offset': (page-1)*48,
                    'limit': 48,
                },
                'correctQuery': True,
                'getFastCategories': True,
                'fastCategoriesLimit': 11,
                'fastCategoriesLevelOffset': 1,
                'getPromotionItems': True,
            },
        },
        'query': 'query getMakeSearch($queryInput: MakeSearchQueryInput!) {\n  makeSearch(query: $queryInput) {\n    id\n    queryId\n    queryText\n    category {\n      ...CategoryShortFragment\n      __typename\n    }\n    categoryTree {\n      category {\n        ...CategoryFragment\n        __typename\n      }\n      total\n      __typename\n    }\n    items {\n      adMarker {\n        orgInn\n        marker\n        orgName\n        __typename\n      }\n      catalogCard {\n        __typename\n        ...SkuGroupCardFragment\n      }\n      bidId\n      __typename\n    }\n    facets {\n      ...FacetFragment\n      __typename\n    }\n    total\n    mayHaveAdultContent\n    categoryFullMatch\n    offerCategory {\n      title\n      id\n      __typename\n    }\n    correctedQueryText\n    categoryWasPredicted\n    fastCategories {\n      category {\n        ...FastCategoryFragment\n        __typename\n      }\n      total\n      __typename\n    }\n    token\n    __typename\n  }\n}\n\nfragment FacetFragment on Facet {\n  filter {\n    id\n    title\n    type\n    measurementUnit\n    description\n    __typename\n  }\n  buckets {\n    filterValue {\n      id\n      description\n      image\n      name\n      __typename\n    }\n    total\n    __typename\n  }\n  range {\n    min\n    max\n    __typename\n  }\n  __typename\n}\n\nfragment CategoryFragment on Category {\n  id\n  icon\n  parent {\n    id\n    __typename\n  }\n  seo {\n    header\n    metaTag\n    __typename\n  }\n  title\n  adult\n  __typename\n}\n\nfragment CategoryShortFragment on Category {\n  id\n  parent {\n    id\n    title\n    __typename\n  }\n  title\n  __typename\n}\n\nfragment FastCategoryFragment on Category {\n  id\n  parent {\n    id\n    title\n    __typename\n  }\n  title\n  seo {\n    header\n    metaTag\n    __typename\n  }\n  __typename\n}\n\nfragment SkuGroupCardFragment on SkuGroupCard {\n  ...DefaultCardFragment\n  photos {\n    key\n    link(trans: PRODUCT_540) {\n      high\n      low\n      __typename\n    }\n    previewLink: link(trans: PRODUCT_240) {\n      high\n      low\n      __typename\n    }\n    __typename\n  }\n  badges {\n    ... on BottomTextBadge {\n      backgroundColor\n      description\n      id\n      link\n      text\n      textColor\n      __typename\n    }\n    __typename\n  }\n  characteristicValues {\n    id\n    value\n    title\n    characteristic {\n      values {\n        id\n        title\n        value\n        __typename\n      }\n      title\n      id\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DefaultCardFragment on CatalogCard {\n  adult\n  favorite\n  feedbackQuantity\n  id\n  minFullPrice\n  minSellPrice\n  offer {\n    due\n    icon\n    text\n    textColor\n    __typename\n  }\n  badges {\n    ... on BottomTextBadge {\n      backgroundColor\n      description\n      id\n      link\n      text\n      textColor\n      __typename\n    }\n    __typename\n  }\n  ordersQuantity\n  productId\n  rating\n  title\n  __typename\n}',
    }
    async with session.post('https://graphql.kazanexpress.ru/', headers=headers, json=json_data) as response:
        return await response.json()

async def getProduct(id, session):

    headers = {
        'authority': 'graphql.kazanexpress.ru',
        'accept': '*/*',
        'accept-language': 'ru',
        'apollographql-client-name': 'web-customers',
        'apollographql-client-version': '1.45.2',
        'authorization': 'Basic a2F6YW5leHByZXNzLWN1c3RvbWVyOmN1c3RvbWVyU2VjcmV0S2V5',
        'baggage': 'sentry-environment=production,sentry-release=kazanexpress%401.45.2,sentry-public_key=84ead3051db54dd6a2ef8f9bc40a9f8b,sentry-trace_id=4b7f5a78fe8040a5a44edf807b3372e1,sentry-sample_rate=0.001,sentry-transaction=product,sentry-sampled=false',
        'content-type': 'application/json',
        'origin': 'https://kazanexpress.ru',
        'referer': 'https://kazanexpress.ru/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sentry-trace': '4b7f5a78fe8040a5a44edf807b3372e1-856ac9235fb8669e-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-iid': 'cb39d276-0fea-45ae-b08f-f9b6224da827',
    }
    json_data = {
        'operationName': 'ProductPage',
        'variables': {
            'productId': id,
            'linkTrans4': 'PRODUCT_240',
            'linkTrans5': 'PRODUCT_240',
            'linkTrans6': 'PRODUCT_240',
            'linkTrans7': 'PRODUCT_240',
        },
        'query': 'query ProductPage($productId: Int!, $linkTrans4: Transformation!, $linkTrans6: Transformation!, $linkTrans5: Transformation!, $linkTrans7: Transformation!) {\n  product(id: $productId) {\n    ordersQuantity\n    feedbackQuantity\n    comments {\n      value\n      type\n      __typename\n    }\n    photo360 {\n      key\n      link(trans: PRODUCT_720) {\n        high\n        low\n        __typename\n      }\n      __typename\n    }\n    photos {\n      key\n      link(trans: PRODUCT_720) {\n        high\n        low\n        __typename\n      }\n      __typename\n    }\n    rating\n    video {\n      key\n      url\n      __typename\n    }\n    title\n    id\n    category {\n      id\n      parentList {\n        id\n        title\n        __typename\n      }\n      title\n      __typename\n    }\n    minFullPrice\n    minSellPrice\n    characteristics {\n      id\n      title\n      type\n      values {\n        id\n        photo {\n          key\n          link(trans: PRODUCT_240) {\n            high\n            low\n            __typename\n          }\n          __typename\n        }\n        title\n        value\n        characteristic {\n          id\n          title\n          type\n          values {\n            id\n            photo {\n              link(trans: $linkTrans7) {\n                high\n                low\n                __typename\n              }\n              key\n              __typename\n            }\n            title\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    badges {\n      ... on BottomIconTextBadge {\n        backgroundColor\n        description\n        iconLink\n        id\n        link\n        text\n        textColor\n        __typename\n      }\n      ... on BottomTextBadge {\n        backgroundColor\n        description\n        id\n        link\n        text\n        textColor\n        __typename\n      }\n      ... on TopTextBadge {\n        backgroundColor\n        id\n        text\n        textColor\n        __typename\n      }\n      __typename\n    }\n    description\n    favorite\n    shop {\n      avatar {\n        low\n        __typename\n      }\n      feedbackQuantity\n      id\n      official\n      ordersQuantity\n      rating\n      seller {\n        accountId\n        legalRecords {\n          name\n          value\n          __typename\n        }\n        __typename\n      }\n      shortTitle\n      title\n      url\n      __typename\n    }\n    shortDescription\n    skuList {\n      id\n      availableAmount\n      photo {\n        key\n        link(trans: $linkTrans4) {\n          low\n          __typename\n        }\n        __typename\n      }\n      paymentOptions {\n        paymentInfo\n        text\n        type\n        id\n        active\n        titleBanner\n        __typename\n      }\n      skuTitle\n      sellPrice\n      properties {\n        description\n        filter {\n          description\n          id\n          measurementUnit\n          title\n          type\n          __typename\n        }\n        id\n        image\n        name\n        __typename\n      }\n      discountBadge {\n        backgroundColor\n        id\n        text\n        textColor\n        __typename\n      }\n      characteristicValues {\n        id\n        photo {\n          key\n          link(trans: $linkTrans6) {\n            low\n            __typename\n          }\n          __typename\n        }\n        title\n        value\n        characteristic {\n          id\n          title\n          type\n          values {\n            id\n            photo {\n              key\n              link(trans: $linkTrans5) {\n                high\n                low\n                __typename\n              }\n              __typename\n            }\n            title\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      fullPrice\n      vat {\n        vatRate\n        vatAmount\n        type\n        price\n        __typename\n      }\n      discountTimer {\n        endDate\n        image {\n          high\n          low\n          __typename\n        }\n        text\n        textColor\n        __typename\n      }\n      __typename\n    }\n    attributes\n    __typename\n  }\n  productPage(id: $productId) {\n    reviewsPhotoAmount\n    actions {\n      location\n      type\n      ... on MotivationAction {\n        image {\n          low\n          high\n          __typename\n        }\n        location\n        text\n        type\n        __typename\n      }\n      ... on WishSaleAction {\n        dateEnd\n        location\n        pressed\n        pressedCount\n        type\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}',
    }

    async with session.post('https://graphql.kazanexpress.ru/', headers=headers, json=json_data) as response:
        return await response.json()


async def get_mouses(page, session):
    response = await getPage(page, session)
    mouses = []
    for i, item in enumerate(response["data"]["makeSearch"]["items"]):
        id = item["catalogCard"]["productId"]
        available_amount = 0
        try:
            available_amount = await getProduct(id, session)
            available_amount = available_amount["data"]["product"]["skuList"][0]["availableAmount"]
        except:
            pass
        data = \
            {
                "name": item["catalogCard"]["title"],
                "price": item["catalogCard"]["minSellPrice"] // 100,
                "old_price": item["catalogCard"]["minFullPrice"] // 100,
                "rating": item["catalogCard"]["rating"],
                "estimates_count": item["catalogCard"]["feedbackQuantity"],
                "product_id": id,
                "link": "https://kazanexpress.ru/product/" + str(id),
                "available_amount": available_amount
            }
        mouses.append(data)
    return mouses

async def gather_data():
    async with aiohttp.ClientSession() as session:
        count_of_products =await getPage(1,session)
        count_of_products = count_of_products["data"]["makeSearch"]["total"]
        count_of_pages = count_of_products // 48 + (1 if count_of_products % 48 == 0 else 2)
        tasks = []

        for page in range(1, count_of_pages):
            task = asyncio.create_task(get_mouses(page, session))
            tasks.append(task)
        data = await asyncio.gather(*tasks)
        with open("mouses.json", "w", encoding='utf-8') as file:
            json.dump([x for y in data for x in y], file)

asyncio.run(gather_data())

