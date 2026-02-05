
# Skill: Transcribe Audio

## Description
Downloads a video/audio file and transcribes the content to text using the Transcription MCP server.

## Input Contract (Pydantic Model)
```python
    class TranscribeInput(BaseModel):
        media_url: str
        language: str = "en"
        diarize: bool = False  # Identify speakers
```

## Output Contract (Pydantic Model)

```python
    class TranscribeOutput(BaseModel):
        text: str
        duration_seconds: float
        word_timestamps: Optional[List[dict]] = None
```

## MCP Tool Required
`mcp-server-media`: Tool `transcribe_audio`