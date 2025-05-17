# 🎓 UniAssist – LLM-Powered Conversational Assistant for University Support

UniAssist is an intelligent, modular chatbot designed to streamline student and faculty support services at Northeastern University – Toronto campus. Powered by cutting-edge LLMs and semantic search technology, it enables personalized, 24/7 assistance across academic and administrative queries.

---

## 🚀 Features

- ✅ Context-aware natural conversations
- 🔍 Semantic search using vector databases (FAISS/ChromaDB)
- 📄 Integration with scraped university policies, program pages, and events
- 💬 Memory-based personalization and proactive suggestions
- 🔌 Tool-based modular architecture (search, events, scraping, documents)
- 🌐 FastAPI-powered backend with RESTful endpoints
- 📊 Real-time analytics and insights (planned)

---

## 📁 Project Structure

uniassist/ │ ├── app.py # FastAPI main entry ├── requirements.txt # Python dependencies ├── README.md # Project documentation │ ├── data/ # Scraped JSON pages ├── vector_store/ # Vector DB files (e.g., FAISS index) │ ├── llm/ # LLM logic and orchestration │ ├── llm_controller.py │ ├── tool_dispatcher.py │ ├── conversation_manager.py │ ├── context_builder.py │ └── response_processor.py │ ├── tools/ # Modular tools the LLM can use │ ├── knowledge_tool.py │ ├── search_tool.py │ ├── document_tool.py │ └── tool_registry.py │ ├── memory/ # Memory + session state handling │ ├── memory_manager.py │ └── state_manager.py │ ├── scraping/ # Crawlers & scrapers │ ├── uni_docs_scraper.py │ ├── events_scraper.py │ └── scheduler.py
