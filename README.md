# Backend-AI-Infrastructure-for-AI-Powered-Digital-Scale-System
This repository contains the software infrastructure of the system

---

## Overview

The AI-Powered Digital Scale System is designed to collect, process, and analyze weight data in real time. It bridges the gap between physical hardware and intelligent software by combining embedded systems with local Large Language Models (LLM).

This repository focuses on the software, backend, and AI layers of the ecosystem.

---

## System Architecture

The data flows through the system in the following sequence:

1. **Hardware Layer**: Load Cell Sensor -> Microcontroller (ESP32 / Arduino).
2. **Transport Layer**: Data transmission via MQTT Broker (Mosquitto).
3. **Backend Layer**: Flask API processes incoming data and manages logic.
4. **Storage & Workflow**: Data is stored in PostgreSQL and managed through n8n Automation.
5. **Intelligence Layer**: Data analysis and response generation via Ollama (Llama 3.2).

---

## Tech Stack

* **Backend**: Python (Flask)
* **Database**: PostgreSQL
* **AI Engine**: Ollama (Local LLM)
* **Automation**: n8n
* **Communication**: MQTT (Mosquitto)
* **Infrastructure**: Docker & Docker Compose
* **Network**: Cloudflare Tunnel

---

## AI Integration

The system utilizes a local AI model to enable smart interpretation of weight data without relying on external cloud APIs.

* **Model**: Llama 3.2 (via Ollama)
* **Integration**: Flask API interfaces with the local AI inference service.
* **Capabilities**: Rule-based automation, weight trend interpretation, and a foundation for predictive analytics.

---

## Hardware Compatibility

The system is hardware-agnostic and follows standard data communication standards.

* **Supported Devices**: ESP32, Arduino, Raspberry Pi, and Industrial PLCs (via protocol bridge).
* **Hardware Requirements**: Sensors (e.g., load cells) must be interfaced through ADC modules such as the HX711.
* **Connectivity**: Devices must have network capabilities or use a gateway to communicate via MQTT.

---

## Key Features

* **Real-time Monitoring**: Continuous collection and processing of weight data.
* **IoT Ready**: Reliable communication using the industry-standard MQTT protocol.
* **Local AI**: Intelligent analysis and data interpretation using on-premise LLMs.
* **Workflow Automation**: Flexible task orchestration via n8n.
* **Containerized**: Consistent deployment using Docker.

---

## API Reference

### POST /chat
Submits a prompt to the AI module for weight data analysis or general queries.

**Request Body:**
```json
{
  "prompt": "Analyze weight trend from the last 10 entries"
}
```

**Response:**
```json
{
  "text": "Analysis result from AI",
  "model": "llama3.2",
  "status": "success"
}
```

---

## Deployment

To deploy the entire stack using Docker Compose, execute the following command:

```bash
docker-compose up -d
```

### Environment Variables

| Variable | Description | Default Value |
| --- | --- | --- |
| OLLAMA_API | Endpoint for AI inference | http://host.docker.internal:11434 |
| MODEL_NAME | The LLM model to be used | llama3.2 |

---

## Future Improvements

* AI-based weight and inventory forecasting.
* Pattern recognition for automated object classification.
* Advanced web-based dashboard for data visualization.
* Integration with enterprise cloud platforms (AWS / GCP).

---

## Project Goal

To provide a scalable AI + IoT framework suitable for industrial applications, including smart factories, automated logistics, and intelligent inventory tracking.

