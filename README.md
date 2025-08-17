# Semantic Kernel Agent Sequential Orchestration

A Python application demonstrating sequential agent orchestration using Microsoft's Semantic Kernel framework with Azure OpenAI. This project showcases how multiple AI agents can work together in a pipeline to process tasks collaboratively.

## 🌟 Features

- **Sequential Agent Processing**: Agents work in a pipeline, where each agent's output becomes the next agent's input
- **Marketing Pipeline**: Complete marketing workflow from analysis to final copy
- **Document Processing**: Bonus example showing summarization and translation
- **Azure OpenAI Integration**: Uses Azure OpenAI services with GPT-4o model
- **Simple Setup**: Hard-coded credentials for quick testing (demo purposes)

## 📋 Prerequisites

- Python 3.8 or higher
- Azure OpenAI subscription and deployment
- Required Python packages (see Installation section)

## 🚀 Installation

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
   ```powershell
   python -m venv labenv
   .\labenv\Scripts\Activate.ps1
   ```

3. **Install required packages**:
   ```powershell
   pip install semantic-kernel
   ```

4. **Update Azure OpenAI credentials** in `app.py`:
   ```python
   service = AzureChatCompletion(
       service_id="default",
       deployment_name="your-deployment-name",
       endpoint="your-azure-openai-endpoint",
       api_key="your-api-key",
   )
   ```

## 🎯 Usage

Run the application:

```powershell
python app.py
```

The application will execute two examples:

### 1. Marketing Pipeline
- **Analyst Agent**: Analyzes product features, target audience, and USPs
- **Copywriter Agent**: Creates compelling marketing copy
- **Editor Agent**: Polishes and refines the final copy

### 2. Document Processing Pipeline
- **Summarizer Agent**: Creates concise summaries
- **Translator Agent**: Translates content to Spanish

## 🏗️ Architecture

### Agent Flow
```
Input → Agent 1 → Agent 2 → Agent 3 → Final Output
```

Each agent:
1. Receives input from the previous agent (or initial input)
2. Processes the content according to its specialized instructions
3. Passes output to the next agent in the sequence

### Key Components

- **Kernel Setup**: Configures Semantic Kernel with Azure OpenAI
- **Agent Creation**: Defines specialized agents with specific instructions
- **Sequential Processing**: Orchestrates agent communication
- **Error Handling**: Includes test functions and error management

## 📁 Project Structure

```
Semantic-Kernel-Agent-Sequential-Orchestration/
├── app.py              # Main application file
├── README.md           # This file
└── labenv/             # Virtual environment (if created)
    ├── Scripts/        # Environment activation scripts
    └── Lib/           # Installed packages
```

## 🔧 Configuration

### Azure OpenAI Settings
Update these values in `app.py`:

```python
deployment_name="gpt-4o"  # Your Azure OpenAI deployment name
endpoint="https://your-resource.openai.azure.com/"  # Your endpoint
api_key="your-api-key"  # Your API key
```

### Agent Instructions
Each agent has customizable instructions. Modify them in the `create_marketing_agents()` function:

```python
analyst_agent = ChatCompletionAgent(
    service=service,
    name="Analyst",
    instructions="Your custom instructions here...",
)
```

## 💡 Examples

### Marketing Pipeline Input
```
"An eco-friendly stainless steel water bottle that keeps drinks cold for 24 hours 
and hot for 12 hours. Features leak-proof design, comes in 5 colors, made from 90% recycled materials."
```

### Expected Output Flow
1. **Analyst**: Identifies eco-friendly features, target audience (environmentally conscious consumers), USPs (temperature retention, sustainability)
2. **Copywriter**: Creates engaging marketing copy highlighting these points
3. **Editor**: Polishes grammar, tone, and clarity for final publication

## 🛠️ Customization

### Adding New Agents
```python
def create_custom_agents(kernel: Kernel) -> List[ChatCompletionAgent]:
    service = kernel.get_service("default")
    
    new_agent = ChatCompletionAgent(
        service=service,
        name="YourAgentName",
        instructions="Your agent's specific instructions...",
    )
    
    return [new_agent]
```

### Modifying the Pipeline
Update the `run_sequential_agents()` function to change how agents communicate or add parallel processing capabilities.

## 🚨 Important Notes

- **Security**: The current implementation uses hard-coded credentials for demonstration purposes only
- **Production Use**: Store credentials securely using environment variables or Azure Key Vault
- **Rate Limits**: Be aware of Azure OpenAI rate limits when scaling up
- **Costs**: Monitor Azure OpenAI usage to control costs

## 🔒 Security Best Practices

For production use:

1. **Environment Variables**:
   ```python
   import os
   api_key = os.getenv("AZURE_OPENAI_API_KEY")
   endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
   ```

2. **Azure Key Vault** for credential management

3. **Managed Identity** for Azure resource authentication

## 📊 Monitoring and Logging

Consider adding:
- Structured logging for agent interactions
- Performance metrics tracking
- Error reporting and alerting
- Cost monitoring for Azure OpenAI usage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational and demonstration purposes. Please ensure compliance with Azure OpenAI terms of service and your organization's policies.

## 🆘 Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify Azure OpenAI credentials
   - Check endpoint URL format
   - Ensure deployment name matches Azure configuration

2. **Package Import Errors**
   - Verify semantic-kernel installation
   - Check Python version compatibility
   - Activate virtual environment

3. **Agent Response Issues**
   - Review agent instructions for clarity
   - Check Azure OpenAI model availability
   - Monitor rate limits and quotas

### Getting Help

- Check Azure OpenAI documentation
- Review Semantic Kernel GitHub repository
- Verify network connectivity to Azure services

## 🔄 Future Enhancements

- [ ] Add parallel agent processing
- [ ] Implement agent memory/context sharing
- [ ] Add web interface for real-time interaction
- [ ] Include more specialized agent types
- [ ] Add conversation history management
- [ ] Implement agent performance metrics

---

**Built with Microsoft Semantic Kernel** 🧠✨
