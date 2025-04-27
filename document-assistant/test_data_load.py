import data_load as DL

TEST_DOCUMENTS_PATH:str = "./documents"   # local folder

def test__load_documents_from_folder():
    loaded_files_and_docs = DL.load_documents_from_folder(documents_folder_path=TEST_DOCUMENTS_PATH)
    
    files_count:int = len(loaded_files_and_docs)
    assert files_count == 2

    for dict_item in loaded_files_and_docs:
        loaded_docs = dict_item['documents']
        docs_count:int = len(loaded_docs) 
        assert docs_count > 0

def test__chunk_text():
    test_text = """
Why Is Nvidia (NVDA) Stock Rocketing Higher Today
Max Juang /
2025/04/09 2:15 pm EDT
What Happened?
Shares of leading designer of graphics chips Nvidia (NASDAQ:NVDA) jumped 15.7% in the afternoon session after markets rallied sharply on news that President Trump announced a 90-day tariff pause. Reciprocal tariffs were also dropped to 10% for most countries, sparking renewed optimism amid ongoing trade talks. The major stock indices rose as investors, growing impatient of seemingly irrational tariff actions, welcomed the pause as a sign of a more measured path forward. 

However, Trump was quick to note that China was not part of the pause. Instead, he prepared to raise tariffs on Chinese goods to 125% after China announced retaliatory tariffs on US imports. This tough stance on China stood in sharp contrast to the softer tone toward others. In a week marked by growing uncertainty, this news eased some of the pressure. The questions remain whether we are out of the woods and can sustain the rally or not.

The shares closed the day at $114.24, up 18.1% from previous close.

Is now the time to buy Nvidia? Access our full analysis report here, it’s free.

What The Market Is Telling Us?
Nvidia’s shares are extremely volatile and have had 33 moves greater than 5% over the last year. In that context, today’s move indicates the market considers this news meaningful but not something that would fundamentally change its perception of the business.

The previous big move we wrote about was 5 days ago when the stock dropped 7.8% on the news that China imposed a 34% tariff on all U.S. imports amid escalating trade war tensions. This was especially rough for the US chipmakers because a big chunk of their business leans on demand out of China. The new tariffs not only threaten to erode profit margins but also risk reducing market share. 

Adding to the uncertainty, the Trump administration signaled the possibility of further regulatory action against the sector. Although semiconductor firms were notably excluded from the broad tariffs unveiled on April 2, 2025, their exclusion raised concerns that targeted restrictions could still be forthcoming.

Nvidia is down 17.6% since the beginning of the year, and at $113.90 per share, it is trading 23.8% below its 52-week high of $149.43 from January 2025. Investors who bought $1,000 worth of Nvidia’s shares 5 years ago would now be looking at an investment worth $17,326.

Do you want to know what moves the business you care about? Add them to your StockStory watchlist and every time a stock significantly moves, we provide you with a timely explanation straight to your inbox. It’s free and will only take you a second.
                """
    loaded_docs = DL.chunk_text(text=test_text)
    docs_count:int = len(loaded_docs) 
    assert docs_count > 0
