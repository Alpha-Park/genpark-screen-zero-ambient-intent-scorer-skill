# -*- coding: utf-8 -*-
"""
Example usage of GlanceScreenZeroAmbientIntentScorer
Demonstrates 3 real-world Screen Zero micro-moments.
"""

from client import GlanceScreenZeroAmbientIntentScorer

def main():
    scorer = GlanceScreenZeroAmbientIntentScorer()

    scenarios = [
        {
            "name": "Scenario 1: Evening Relaxation Leisure Dwell (High Intent)",
            "dwell": 3.8,
            "vel": 80.0,
            "angle": 10.0,
            "hour": 21,
            "freq": 6,
            "affinities": {"Luxury Apparel": 0.88, "Beauty & Skincare": 0.75, "Consumer Tech": 0.40}
        },
        {
            "name": "Scenario 2: Morning Rush Rapid Unlock (Low Intent)",
            "dwell": 0.6,
            "vel": 850.0,
            "angle": 85.0,
            "hour": 8,
            "freq": 2,
            "affinities": {"Luxury Apparel": 0.30, "Fast Delivery Food": 0.70}
        },
        {
            "name": "Scenario 3: Lunchtime Active Browsing (Moderate Intent)",
            "dwell": 2.2,
            "vel": 180.0,
            "angle": 25.0,
            "hour": 12,
            "freq": 4,
            "affinities": {"Designer Sunglasses": 0.82, "Athletic Footwear": 0.79}
        }
    ]

    print("================================================================")
    print("Glance Screen Zero Ambient Intent Scorer - Live Test Cases")
    print("================================================================\n")

    for sc in scenarios:
        res = scorer.score_ambient_intent(
            dwell_time_sec=sc["dwell"],
            swipe_velocity_px_s=sc["vel"],
            swipe_angle_deg=sc["angle"],
            wake_hour_of_day=sc["hour"],
            wake_frequency_last_hour=sc["freq"],
            historical_category_affinities=sc["affinities"]
        )
        print(f"[{sc['name']}]")
        print(f"  Composite Intent Score : {res['composite_intent_score']} / 100 ({res['intent_confidence_tier']})")
        print(f"  Attention Grade        : {res['attention_grade']}")
        print(f"  Recommended Action     : {res['recommended_screen_zero_action']}")
        print(f"  Top Category Target    : {res['top_predicted_category']}")
        print(f"  Component Breakdown    : Attention={res['components']['dwell_attention_score']}, Physics={res['components']['swipe_physics_score']}, Circadian={res['components']['circadian_hourly_bias']}\n")

if __name__ == "__main__":
    main()
