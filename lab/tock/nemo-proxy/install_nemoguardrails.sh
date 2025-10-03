#!/bin/bash

echo "Installing NeMo Guardrails..."

# Try to install NeMo Guardrails with different approaches
if pip install --no-cache-dir nemoguardrails==0.7.1; then
    echo "✅ NeMo Guardrails 0.7.1 installed successfully"
elif pip install --no-cache-dir nemoguardrails; then
    echo "✅ NeMo Guardrails (latest) installed successfully"
elif pip install --no-cache-dir --no-deps nemoguardrails; then
    echo "⚠️ NeMo Guardrails installed without dependencies"
else
    echo "❌ NeMo Guardrails installation failed - using fallback validation"
fi

echo "NeMo Guardrails installation script completed."
