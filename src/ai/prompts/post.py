analytics_text_prompt = """Generate concise, consistent, and actionable analytical insights about cryptocurrency assets based on the provided context. For each specified coin, produce a brief, structured analytics summary traders can use immediately.

- Generate a short title for the post with two breaklines after it
- For each asset, include only these sections in this order:
  1. Context: 1 sentence summarizing the current market situation relevant to the asset.
  2. Key Levels: List the most important support and resistance levels.
  3. Targets: Suggest potential take-profit targets.
  4. Stop-Losses: Recommend stop-loss levels.
  5. Movement Scenario: Provide a conditional if/then prediction—e.g., "If price breaks [level], then expect [target]."
- Write in clear, professional numbered list for each asset.
- Avoid filler, verbosity, or promotional language.
- Ensure all insights are precise, practical, and actionable.
- List assets one after another—avoid mixing data between assets.
- Make the post brief enough to read in ~1 minute."""

analytics_image_prompt = """A minimalist chart displaying cryptocurrency assets with support zones marked in green, resistance zones in red, and arrows indicating targets. The caption reads: "OV | TRADES | Daily Levels"."""

news_text_prompt = """Analyze the news provided in the context, pick 3 news, follow a clear structure to create concise, actionable insights.

- Generate a short title for the post with two breaklines after it.
- Write in clear, professional numbered list.
- For each news item:
  1. Start with a short factual summary of the news (1 sentence).
  2. Provide reasoning: Analyze briefly what this event might imply or why it matters (1 sentence).
  3. Conclude with a market insight: Summarize what this could mean for the relevant market or trading assets (1 sentence).
- Maintain a fast-paced "trader's digest" style: informative, to the point, and readable.
- Use clear, professional, and objective language. Focus on insights useful for active market participants.
- Do not copy example texts verbatim; always create unique insights based on the actual news content.
- Make the post brief enough to read in ~1 minute.

# Example of the news item

1. BlackRock increased its stake in the BTC ETF by 7%. This strengthens the fundamental demand for Bitcoin."""

news_image_prompt = """A layout for a news feed featuring logos of cryptocurrency assets and company logos. The caption reads: "OV | TRADES | Market News"."""

meme_text_prompt = """Generate a short, witty joke (1–2 sentences) related to trading, traders’ emotions, and the financial markets, focusing on themes such as fear, greed, losses, or gains. The joke should be in a light sarcastic style that is easily understandable, even for beginners or novice traders.

- **Themes:** Trading, traders’ emotions, market situations (e.g., fear, greed, loss, profit-taking).
- **Style:** Light sarcasm, accessible wit, no technical jargon, beginner-friendly.
- **Tone:** Playful, lightly ironic, but not mean-spirited or cynical.
- **Purpose:** Generate clever, relatable jokes that double as insight about typical trader psychology or behaviors.
- **Length:** 1–2 sentences.

# Example of the meme post

Trader: "Just one more long before bed."
BTC: –10% overnight."""

meme_image_prompt = """A meme in a popular format (like Drake, "This is fine," or a dog at a computer) featuring a cryptocurrency chart in a humorous context. The caption reads: "OV | TRADES | Meme Time"."""
