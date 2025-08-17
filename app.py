"""
Simple Semantic Kernel Sequential Agent Example
Based on Microsoft's official patterns for agent orchestration

Prerequisites:
- pip install semantic-kernel
- Azure OpenAI credentials (hard-coded below)
"""

import asyncio
from typing import List

from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatHistory


def setup_kernel() -> Kernel:
    """Setup Semantic Kernel with Azure OpenAI service."""
    kernel = Kernel()
    
    # Hard-coded Azure OpenAI Configuration
    service = AzureChatCompletion(
        service_id="default",
        deployment_name="",
        endpoint="",
        api_key="",
    )
    
    kernel.add_service(service)
    return kernel


def create_marketing_agents(kernel: Kernel) -> List[ChatCompletionAgent]:
    """Create agents for the marketing pipeline."""
    
    service = kernel.get_service("default")
    
    # Agent 1: Marketing Analyst
    analyst_agent = ChatCompletionAgent(
        service=service,
        name="Analyst",
        instructions="""You are a marketing analyst. Given a product description, identify:
- Key features
- Target audience  
- Unique selling points

Provide your analysis in a clear, structured format.""",
    )
    
    # Agent 2: Copywriter
    copywriter_agent = ChatCompletionAgent(
        service=service,
        name="Copywriter", 
        instructions="""You are a marketing copywriter. Given analysis of features, audience, and USPs, 
compose compelling marketing copy (like a newsletter section) that highlights these points. 
Output should be around 150 words, engaging and persuasive.""",
    )
    
    # Agent 3: Editor
    editor_agent = ChatCompletionAgent(
        service=service,
        name="Editor",
        instructions="""You are an editor. Given draft copy, correct grammar, improve clarity, 
ensure consistent tone, and make it polished. Output the final improved copy.""",
    )
    
    return [analyst_agent, copywriter_agent, editor_agent]


async def run_sequential_agents(agents: List[ChatCompletionAgent], input_text: str) -> str:
    """Run agents sequentially, passing output from one to the next."""
    
    current_input = input_text
    print(f"🚀 Starting with input: {input_text}\n")
    
    for i, agent in enumerate(agents, 1):
        print(f"🤖 Step {i}: {agent.name}")
        print("-" * 50)
        
        # Create chat history for this agent
        chat_history = ChatHistory()
        chat_history.add_user_message(current_input)
        
        # Get response from agent
        async for response in agent.invoke(chat_history):
            agent_output = str(response)
            print(f"{agent_output}")
            current_input = agent_output  # Use this output as input for next agent
            break  # Take only the first response
        
        print("-" * 50)
        print()
    
    return current_input


async def test_single_agent():
    """Simple test to verify agent setup works."""
    print("🧪 Testing Single Agent...")
    print("=" * 60)
    
    try:
        kernel = setup_kernel()
        service = kernel.get_service("default")
        
        test_agent = ChatCompletionAgent(
            service=service,
            name="TestAgent",
            instructions="You are a helpful assistant. Answer questions clearly and briefly.",
        )
        
        chat_history = ChatHistory()
        chat_history.add_user_message("What is 2+2? Just give me the number.")
        
        async for response in test_agent.invoke(chat_history):
            print(f"✅ Test Response: {response}")
            break
            
        print("🎉 Single agent test successful!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


async def main():
    """Main function demonstrating sequential agent orchestration."""
    
    print("🌟 Simple Semantic Kernel Sequential Agents")
    print("✅ Using hard-coded Azure OpenAI credentials")
    print("=" * 60)
    
    # Test single agent first
    if not await test_single_agent():
        print("❌ Single agent test failed. Cannot proceed.")
        return
    
    print("\n" + "=" * 60)
    print("📈 Marketing Pipeline Example")
    print("=" * 60)
    
    try:
        # Setup
        kernel = setup_kernel()
        agents = create_marketing_agents(kernel)
        
        # Input product description
        product_description = """An eco-friendly stainless steel water bottle that keeps drinks cold for 24 hours 
and hot for 12 hours. Features leak-proof design, comes in 5 colors, made from 90% recycled materials."""
        
        # Run sequential processing
        final_result = await run_sequential_agents(agents, product_description)
        
        print("🎉 FINAL MARKETING COPY:")
        print("=" * 60) 
        print(final_result)
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Error in main pipeline: {e}")


async def document_example():
    """Bonus example: Document processing pipeline."""
    print("\n" + "=" * 60)
    print("📄 Document Processing Example")
    print("=" * 60)
    
    try:
        kernel = setup_kernel()
        service = kernel.get_service("default")
        
        # Create document processing agents
        summarizer = ChatCompletionAgent(
            service=service,
            name="Summarizer",
            instructions="Summarize the given text in under 100 words, highlighting key points.",
        )
        
        translator = ChatCompletionAgent(
            service=service,
            name="Translator", 
            instructions="Translate the given English text to Spanish, maintaining meaning and tone.",
        )
        
        doc_agents = [summarizer, translator]
        
        document_text = """Artificial Intelligence has revolutionized industries by automating complex tasks 
and providing intelligent insights. Machine learning analyzes data to identify patterns and predictions. 
Natural language processing enables computers to understand human language. These technologies are 
applied in healthcare, finance, and transportation."""
        
        result = await run_sequential_agents(doc_agents, document_text)
        
        print("📋 PROCESSED DOCUMENT:")
        print("=" * 60)
        print(result)
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Document processing error: {e}")


if __name__ == "__main__":
    """
    Run the sequential agent examples.
    All credentials are hard-coded - no environment setup needed!
    """
    
    # Run main marketing example
    asyncio.run(main())
    
    # Run document processing example  
    asyncio.run(document_example())