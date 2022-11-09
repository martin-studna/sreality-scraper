from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from scrapy.crawler import CrawlerProcess
from srealityspider import SrealitySpider
from flat_post_repository import FlatPostRepository
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


repository = FlatPostRepository()
    

@app.get("/", response_class=HTMLResponse)
async def root():
    results = repository.get_posts(500)
    output = ""
    for i in range(len(results)):
        output += "<div>" + \
            f"<div>{results[i][0]}</div>" + \
            f"<img src={results[i][1]} alt='{i}-image' />" + " </div>"
    
    return output


def main():
    
    
    count = repository.get_count().first()[0]
    
    if count == 0:
        process = CrawlerProcess()
        process.crawl(SrealitySpider, repository)
        process.start()
        
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
