# Backend-AI-Infrastructure-for-AI-Powered-Digital-Scale-System
This repository contains the software infrastructure of the system

# 🤖 AI-Powered Digital Scale System

### Backend & AI Infrastructure

This repository contains the backend and AI infrastructure for an intelligent digital weighing system that integrates IoT devices, real-time communication, and AI-powered processing.

---

## 📌 Overview

This project is an **AI-powered digital weighing system** designed to collect, process, and analyze weight data in real time.

It combines:

* Embedded hardware (load cells, microcontrollers)
* IoT communication (MQTT)
* Backend automation
* AI processing (LLM-based via Ollama)

> 💡 This repository focuses on the **software, backend, and AI layer**

---

## 🧠 AI Integration

This system integrates a local AI model to enable intelligent data processing and future predictive capabilities.

### 🔧 Configuration

* Model: `llama3.2` (via Ollama)
* API: Local AI inference service
* Integration: Flask API → Ollama

### ⚙️ AI Workflow

1. Sensor data is collected from hardware
2. Data is sent via MQTT
3. Backend processes incoming data
4. AI module analyzes or generates responses
5. Results can trigger automation (via n8n)

### 💡 AI Capabilities

* Smart interpretation of weight data
* Rule-based + AI-assisted automation
* Foundation for predictive analytics

---

## 🏗️ System Architecture

```
[ Load Cell Sensor ]
        ↓
[ Microcontroller (ESP32 / Arduino) ]
        ↓
[ MQTT Broker (Mosquitto) ]
        ↓
[ Flask Backend API ]
        ↓
 ┌───────────────┬───────────────┐
 │               │               │
[ PostgreSQL ] [ n8n Automation ] [ Ollama AI ]
```

---

## 🔌 Hardware Compatibility

This system is **hardware-agnostic** and can integrate with any device capable of sending data via MQTT or supported communication protocols.

### ✅ Supported Devices

* ESP32 / Arduino
* Raspberry Pi
* Industrial PLC (via protocol bridge)

### ⚠️ Notes

* Devices without network capability require a gateway (e.g., microcontroller or edge device)
* Sensors (e.g., load cells) must be connected through ADC modules (e.g., HX711)

> 💡 The system focuses on **data communication standards**, not specific hardware models

---

## 📡 Communication Layer

* MQTT (Mosquitto) for real-time data transmission

---

## 🌐 Software & AI Layer (This Repository)

* Flask API for data processing
* PostgreSQL for data storage
* n8n for workflow automation
* Ollama for AI processing
* Cloudflare Tunnel for deployment

---

## ⚙️ Tech Stack

* Python (Flask)
* Docker / Docker Compose
* PostgreSQL
* n8n
* MQTT (Mosquitto)
* Ollama (LLM AI)

---

## 🚀 Features

* 📊 Real-time weight data collection
* 🌐 IoT-based communication
* 🤖 AI-powered processing (LLM integration)
* ⚙️ Automated workflows (n8n)
* 🐳 Containerized deployment (Docker)
* 🔄 Scalable backend architecture

---

## 📡 API Example

### POST `/chat`

```json
{
  "prompt": "Analyze weight trend"
}
```

Response:

```json
{
  "text": "AI response",
  "model": "llama3.2",
  "status": "success"
}
```

---

## 🐳 Deployment

Run the system using Docker Compose:

```bash
docker-compose up -d
```

---

## 🔧 Environment Variables

| Variable   | Description     | Default                           |
| ---------- | --------------- | --------------------------------- |
| OLLAMA_API | AI API endpoint | http://host.docker.internal:11434 |
| MODEL_NAME | AI model        | llama3.2                          |

---

## 🧪 Future Improvements

* 📈 AI-based weight prediction
* 🧠 Pattern recognition from weight data
* 📦 Object classification by weight behavior
* 📊 Dashboard & visualization system
* ☁️ Cloud deployment (AWS / GCP)

---

## 👨‍💻 Role

Designed and developed the system architecture and backend infrastructure:

* Backend API development (Flask)
* AI integration (Ollama)
* Docker-based system deployment
* IoT communication integration (MQTT)
* Workflow automation (n8n)

---

## 🎯 Project Goal

To build a **scalable AI + IoT system** that can be deployed in real-world applications such as:

* Smart factories
* Automated logistics systems
* Intelligent inventory tracking

---

## ⭐ Key Highlight

> This project demonstrates the integration of **AI + IoT + Automation + Backend Engineering** in a real-world system.

