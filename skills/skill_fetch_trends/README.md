# Skill: Fetch Trends
## Description
Queries the News MCP server to fetch the latest headlines relevant to the Agent's persona.

## Input Contract (Pydantic Model)

```class TrendFetchInput(BaseModel):    topic: str    max_results: int = 10    time_range: str = "24h"`

## Output Contract (Pydantic Model)

```python
    class Article(BaseModel):
        title: str
        url: str
        relevance_score: float
        published_at: datetime

    class TrendFetchOutput(BaseModel):
        articles: List[Article]
        total_fetched: int
```

## MCP Tool Required
`mcp-server-news`: Resource `news://latest`