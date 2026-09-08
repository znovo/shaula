# AI Character Framework

An open-source framework for building entertainment-focused AI characters with personality, emotions, memory, voice, and autonomous behavior.

The goal is to create a reusable foundation for multiple AI characters instead of building a single character with a fixed implementation.

## ✨ Features

### Current

* Modular AI agent architecture
* OpenAI-compatible LLM client
* Emotional state system
* Emotion intensity
* Short-term memory
* Character personality system
* Terminal interface
* Screenshot capture
* Voice support

### Planned

* Long-term factual memory
* Semantic memory retrieval (RAG)
* Event-driven mental loop
* Autonomous interactions
* Screen/game observation
* Multiple character configurations
* More advanced emotional transitions
* Additional tools and integrations

## 🧠 Architecture

The project is divided into independent modules:

```text
agent/
├── core/
│   ├── agent.py
│   ├── personality.py
│   └── context.py
│
├── emotion/
│   ├── state.py
│   ├── engine.py
│   ├── rules.py
│   └── manager.py
│
├── memory/
│   ├── short_term.py
│   ├── long_term.py
│   └── rag.py
│
├── mental_loop/
│   ├── loop.py
│   ├── scheduler.py
│   └── triggers.py
│
├── llm/
│   └── client.py
│
├── perception/
│   └── screen.py
│
├── voice/
│   ├── stt.py
│   └── tts.py
│
├── interface/
│   └── terminal.py
│
└── characters/
```

Each module has a specific responsibility, making it possible to replace or extend individual components without rewriting the entire system.

## ❤️ Emotion System

The framework uses five basic emotional states:

* `neutral`
* `joy`
* `sadness`
* `calm`
* `irritation`

Two pairs are opposites:

```text
joy        ↔ sadness
calm       ↔ irritation
```

`neutral` acts as the default state.

Each emotional state has an intensity between `0.0` and `1.0`.

For example:

```python
EmotionState(
    emotion="joy",
    intensity=0.65
)
```

The emotional system is handled by the framework rather than being directly controlled by the LLM.

The LLM receives the current emotional state and uses it to influence how the character responds.

## 🤖 LLM

The framework uses an OpenAI-compatible API.

The LLM client is designed to allow different providers and models to be swapped without changing the rest of the architecture.

```python
LLMClient(
    base_url="...",
    api_key="...",
    model="..."
)
```

This allows the same character framework to work with different compatible providers.

## 🧠 Memory

The memory system is divided into short-term and long-term memory.

### Short-term memory

Stores recent conversation and temporary context.

### Long-term memory

Stores factual information about:

* The user
* The character
* Relationships between the character and other people

The project will eventually include memory decay so that information does not necessarily remain permanently relevant.

## 🔄 Mental Loop

The framework will include a small event-driven mental loop.

Rather than constantly calling the LLM, the loop will process events only when there is a reason to do so.

Possible future triggers include:

```text
User interaction
Game events
Emotion changes
Time-based events
Screen observations
```

The long-term goal is to allow characters to initiate conversations or decide to do something without requiring every action to be directly requested by the user.

## 👁️ Perception

The framework can capture the user's screen for future visual perception.

The current implementation uses PyAutoGUI:

```text
Screen
  ↓
PyAutoGUI
  ↓
Image
  ↓
Resize / Processing
  ↓
Vision model
```

Game observation is planned for a later stage.

## 🔊 Voice

Voice interaction is part of the framework's design from the beginning.

The voice system is divided into:

* `stt.py` for Speech-to-Text
* `tts.py` for Text-to-Speech

This keeps voice providers independent from the core agent.

## 🎭 Characters

Characters are intended to be configurations built on top of the same framework.

For example:

```text
characters/
├── character_a/
├── character_b/
└── character_c/
```

Each character can have its own:

* Name
* Personality
* Behavior
* Voice
* Initial emotional state
* System instructions

The core architecture remains shared.

## 🎯 Project Goal

The goal is not to create a single chatbot.

The goal is to build a framework where different entertainment-focused AI characters can be created using the same underlying systems.

A character should eventually be able to:

* Talk with the user
* Remember relevant information
* React emotionally
* Speak naturally
* Observe activities
* Make spontaneous comments
* Initiate interactions when appropriate
* Use tools autonomously

## 🛠️ Development

This project is being developed as part of **Hack Club Stardance 2026**.

Development is documented through GitHub commits and devlogs.

The project is being built incrementally, starting with a functional core before adding more advanced autonomous behavior.

## 🤖 AI Usage

AI tools are used as development assistants.

### GitHub Copilot

Used for:

* Code autocomplete
* Documentation assistance
* Programming questions
* Bug correction
* Understanding APIs and libraries
* boring tasks

### ChatGPT

Used for:

* Project architecture design
* Discussing technical decisions
* Programming questions
* Reviewing ideas
* Identifying potential problems

AI suggestions are reviewed and integrated manually, and the final architecture and implementation decisions are made by the project developer.

## 📌 Status

**Early development**

The architecture is currently being established. Core systems such as the LLM client, emotions, memory, voice, and agent loop are being implemented incrementally.

This project is experimental and will evolve as new systems are tested.

## 📄 License

MIT
