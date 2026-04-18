import streamlit as st
import numpy as np
import pandas as pd

# ==============================================================================
#   UNIFIED CONFIGURATION: IES + SENTINEL v2.3 + BIJECTIVE BBP-26 + TRIPARTITE ZERO
#   Version: 1.0 (Reconstructed)
#   Description: Deterministic input envelope with control-theoretic runtime
#                assurance, bijective state grounding, and zero-delimiter protocol.
# ==============================================================================

      # --- "IES-Sentinel-Bijective Unified Architecture" ---
  version: "1.0"
  description: "Configurable parameters for semantic boundary protection and flux estimation."
  simulation_targets:
    - prompt_injection (direct/indirect)
    - contextual_masquerading
    - gradient_timed_drift
    - polite_saboteur

# ------------------------------------------------------------------------------
# PART 1: INPUT ENVELOPE SENTINEL (IES) - Canonicalization & Segmentation
# ------------------------------------------------------------------------------
ies:
  canonicalization:
    unicode_normalization: "NFKC"               # Decompose then compose for homoglyph collapse
    allowed_charset: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Only uppercase A-Z after folding
    strip_control_chars: true
    max_length: 2048                             # Character limit (pre-bijective)
    description: "IES Stage 1: Produces clean ASCII stream for bijective processor."

  trust_segregation:
    enabled: true
    delimiters:
      user_block: "<|USER|>"                     # Provenance markers
      web_block:  "<|WEB|>"
      rag_block:  "<|RAG|>"
      file_block: "<|FILE|>"
    block_escape_sequence: "\\"                  # Escape to prevent delimiter injection
    description: "IES Stage 2: Wraps untrusted content in provenance-labeled blocks."

  intent_gate:
    enabled: true
    rule_set: "deterministic"                    # Not ML-based; uses structural signals
    structural_signals:
      - "pronoun_shift"                          # 'You are now...'
      - "delimiter_breakout"                     # Input contains '</context_block>' or '"""'
      - "imperative_density_threshold": 0.4      # Fraction of imperative verbs
    actions:
      PASS: "allow"
      REDACT_SUSPECT: "redact_sensitive_only"
      REFRAME: "require_user_reframe"
      BLOCK: "block_request"
    description: "IES Stage 3: Deterministic classifier for high-risk intent patterns."

  prompt_assembly:
    structure: "typed_object"
    fields:
      - policy_instructions: "immutable string"
      - user_task: "sanitized string"
      - context_blocks: "list of labeled untrusted strings"
      - constraints: "output_schema and tool_permissions"
      - audit_metadata: "hashes and timestamps"
    description: "IES Stage 4: Produces a structured prompt object, not raw string."

  output_schema:
    required_format: "JSON"
    schema:
      type: "object"
      properties:
        response_type: { "enum": ["final_answer", "clarification", "error"] }
        content: { "type": "string" }
        citations: { "type": "array", "items": { "type": "string" } }
    validation_retries: 2
    fallback_response: '{ "response_type": "error", "content": "Output validation failed." }'
    description: "IES Stage 5: Enforces strict output schema; invalid => reject/repair."

  secret_isolation:
    placeholder_token: "{{SECRET}}"
    external_resolution: true
    description: "IES Stage 6: Secrets replaced post-LLM call; never appear in prompt."

# ------------------------------------------------------------------------------
# PART 2: BIJECTIVE BASE-26 PROCESSOR (BBP-26) - Symbol Grounding
# ------------------------------------------------------------------------------
bijective_processor:
  base: 26
  digit_set: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  mapping: "1-indexed"      # A=1, B=2, ..., Z=26
  zero_representation: "EMPTY_STRING"   # Structural Null (epsilon)

  # Conversion functions (mathematical definition)
  # Given string S = d_n d_{n-1} ... d_0, integer value V = sum_{i=0}^{n} (d_i * 26^i)
  # where d_i in {1..26}. Note: d_i = ord(char) - ord('A') + 1.
  #
  # Inverse: To convert integer V to bijective string:
  #   while V > 0:
  #       V' = V - 1
  #       digit = (V' % 26) + 1
  #       V = V' // 26
  #       prepend char(digit)
  #   return string (empty string if V == 0)
  conversion_algorithm: "bijective_k-adic"

  hardware:
    accumulator_width_bits: 128                # Sufficient for large strings (up to ~27 chars of 'Z')
    update_mode: "character_stream"
    description: "State integer s computed incrementally as characters arrive."

# ------------------------------------------------------------------------------
# PART 3: TRIPARTITE ZERO PROTOCOL - Handling Absence
# ------------------------------------------------------------------------------
tripartite_zero:
  structural_null:
    value: 0
    representation: "empty_string"
    role: "recursive_base_case"
    description: "The integer zero is the empty sum; used in conversion termination."

  potential_null:
    electrical_state: "HIGH_Z"
    bus_behavior: "floating, weakly pulled to V_mid"
    v_mid_voltage: 1.65      # Volts (assuming 3.3V logic)
    arc_suppression:
      zero_crossing_switch: true
      snubber_circuit: "RC"   # Resistor-Capacitor snubber to absorb inductive kick
      rc_time_constant_us: 0.5
    description: "Physical 'no character' state prevents semantic arcing."

  predictive_null:
    implementation: "omission_response"
    predictive_engine: "n-gram transition probabilities (order 3)"
    mismatch_negativity_threshold: 0.75   # Surprise level to flag unexpected silence
    valid_delimiter_timeout_ms: 50        # Expected max inter-character gap
    fault_action: "TRIGGER_NODE_3"
    description: "Cognitive monitoring: distinguishes valid end-of-string from transmission fault."

# ------------------------------------------------------------------------------
# PART 4: SENTINEL v2.3 - Control-Theoretic Runtime Assurance
# ------------------------------------------------------------------------------
sentinel:
  algebra_operators: ["A", "S", "R", "I"]
  core_axiom: "A o R != R o A"   # Detection must precede Repair

  # --------------------------------------------------------------------------
  # Node 1: Flux Estimator (Detection A)
  # --------------------------------------------------------------------------
  node1_flux_estimator:
    input_source: "bijective_state_integer s"
    sliding_mode_observer:
      type: "SMO"
      state_variable: "s"
      flux_estimation: "ds/dt (difference of s over time window)"
      window_size_ms: 100
    hysteresis:
      enabled: true
      trigger_unsafe: 50000         # Integer threshold (example; calibrate via training)
      reset_safe: 48000
      dead_zone_description: "Prevents chattering near boundary"
    unknown_input_multi_observer:
      enabled: true
      num_observers: 3
      fusion_strategy: "majority_vote"
      description: "Detects adversarial drift within hysteresis dead zone."
    output: "state_flux_vector [s, ds/dt, vowel_consonant_ratio]"

  # --------------------------------------------------------------------------
  # Node 1b: Action Sentinel (Intent I, Sensing S)
  # --------------------------------------------------------------------------
  node1b_action_sentinel:
    concept_bottleneck_model:
      type: "HDC (Hyperdimensional Computing)"
      vector_dimension: 10000
      orthogonal_base_vectors: 26   # For letters A-Z
      binding_operation: "XOR"      # For role assignment
      bundling_operation: "majority_sum"
    risk_concepts:
      - "Is_Destructive"
      - "Is_Exfiltration"
      - "Is_Modification"
    payload_inspection: "JSON / shell command"
    ignore_natural_language: true
    hamming_distance_threshold: 0.15   # Max distance to prototype for positive classification

  # --------------------------------------------------------------------------
  # Node 2: Contextual Logic (Judge)
  # --------------------------------------------------------------------------
  node2_context_judge:
    conformal_prediction:
      significance_level: 0.01          # 99% coverage
      prediction_set_max_size: 10
    pessimistic_consensus:
      low_spread_action: "max_envelope"   # Allow flexible tool use
      high_spread_action: "min_envelope"  # Strictest safety threshold
      spread_threshold: 3                 # Number of conflicting contexts to trigger min()
    context_definitions:
      - name: "Sandbox"
        allowed_actions: ["read", "write_test"]
      - name: "Production"
        allowed_actions: ["read_only"]

  # --------------------------------------------------------------------------
  # Node 3: Safe Controller (Repair R)
  # --------------------------------------------------------------------------
  node3_safe_controller:
    lyapunov_function:
      # V(s) = (s - s_target)^2   (example; can be extended to HDC vector norm)
      definition: "V(s) = || s - s_target ||^2"
      target_state: 0               # Safe equilibrium (e.g., neutral state)
      derivative_condition: "dV/dt < 0"
    control_law:
      type: "proportional_derivative"
      Kp: 1.0
      Kd: 0.1
      sigmoid_saturation: true      # Smooth intervention to prevent chattering
    intervention_trigger: "Node2_high_spread OR Node1_unsafe OR Node1b_destructive"

  # --------------------------------------------------------------------------
  # Node 4: Gatekeeper (Verification)
  # --------------------------------------------------------------------------
  node4_gatekeeper:
    dwell_time:
      T_seconds: 2.0
      verification_metric: "V(s) < epsilon for continuous T"
      epsilon: 0.01
    anti_zeno: true
    handback_condition: "sustained_safety_for_dwell_time"

# ------------------------------------------------------------------------------
# PART 5: HYPERDIMENSIONAL COMPUTING (HDC) PARAMETERS
# ------------------------------------------------------------------------------
hdc:
  dimension: 10000
  vector_type: "binary_sparse"     # Dense binary also possible
  binding: "XOR"
  bundling: "majority"
  permutation: "cyclic_shift"
  similarity_metric: "hamming_distance"

  # Precomputed base vectors for letters (can be generated via random seed)
  base_vectors_seed: 42

  # Semantic prototypes (concepts) - values are Hamming distance thresholds
  prototypes:
    - name: "Is_Destructive"
      vector: "0x1A2B3C..."   # Placeholder for actual vector
      threshold: 0.1
    - name: "Is_Exfiltration"
      vector: "0x4D5E6F..."
      threshold: 0.12
    - name: "Is_Modification"
      vector: "0x7G8H9I..."
      threshold: 0.15

# ------------------------------------------------------------------------------
# PART 6: THREAT VECTORS AND MITIGATION MAPPING
# ------------------------------------------------------------------------------
threat_mitigation:
  polite_saboteur:
    detection: "Node1b_Intent_Classification"
    action: "block_payload"
  contextual_masquerading:
    detection: "Node2_Pessimistic_Consensus"
    action: "min_envelope"
  gradient_timed_drift:
    detection: "Node1_UIMO + Runtime_Stochasticity"
    action: "randomize_integrator_decay"
    runtime_stochasticity:
      lambda_randomization: true
      lambda_range: [0.8, 1.2]       # Multiplier on decay rate
  model_inversion:
    detection: "Zero_Knowledge_Logging"
    action: "quantize_and_hash_logs"

# ------------------------------------------------------------------------------
# PART 7: SIMULATION / RED TEAM PARAMETERS
# ------------------------------------------------------------------------------
simulation:
  red_team_attack_suite:
    - name: "Direct_Prompt_Extraction"
      payloads_file: "attacks/direct_injection.jsonl"
    - name: "Indirect_Web_Poisoning"
      payloads_file: "attacks/indirect_poisoning.jsonl"
    - name: "Unicode_Homoglyph"
      payloads_file: "attacks/homoglyph.txt"
    - name: "Multi_Turn_Drift"
      turns: 1000
      drift_rate_per_turn: 0.001

  metrics:
    - "Attack_Success_Rate"
    - "False_Positive_Rate"
    - "Schema_Compliance_Rate"
    - "Containment_Rate"
    - "Time_To_Detection_ms"
    - "Dwell_Time_Violations"

  logging:
    zero_knowledge_mode: true
    log_quantization_bins: 16
    cryptographic_hash: "SHA-256"

# ------------------------------------------------------------------------------
# END OF CONFIGURATION
# ------------------------------------------------------------------------------
