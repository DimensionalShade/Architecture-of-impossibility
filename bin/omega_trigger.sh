#!/data/data/com.termux/files/usr/bin/bash

echo "🔍 Estimating Ω..."
omega=$(python omega_trigger.py | grep -oP 'Estimated Ω: \K[0-9.]+')

echo "Estimated Ω: $omega"

threshold=0.500000
above=$(echo "$omega > $threshold" | bc)

if [ "$above" -eq 1 ]; then
  echo "⚠️ Ω exceeds threshold — activating phase"
  python agents/omega.py
else
  echo "✅ Ω below threshold — classical mode continues"
fi
