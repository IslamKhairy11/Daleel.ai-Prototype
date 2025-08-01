# mock_data.py
import pandas as pd

def get_mock_candidates():
    return [
        {
            'id': 'nora_talent',
            'name': 'Nora Ekramy',
            'title': 'AI Engineer',
            'tech_score': 95,
            'culture_score': 88, # 1-100 scale
            'team_fit_preference': 'collaborative',
            'salary_expectation': 30000,
            'past_experience': [
                {'company': 'Youtiva', 'satisfaction': 5, 'reason': 'Great autonomy and impact.'},
                {'company': 'Siemens', 'satisfaction': 4, 'reason': 'Excellent learning, but slow pace.'}
            ],
            'digital_twin_complete': True,
        },
        {
            'id': 'ibrahim_talent',
            'name': 'Ibrahim Khairy',
            'title': 'BIM Specialist',
            'tech_score': 92,
            'culture_score': 91,
            'team_fit_preference': 'structured',
            'salary_expectation': 25000,
            'past_experience': [
                {'company': 'Hassan Allam', 'satisfaction': 4, 'reason': 'Worked on massive projects.'},
                {'company': 'iCareer', 'satisfaction': 3, 'reason': 'Good sales experience.'}
            ],
            'digital_twin_complete': True,
        },
        # Add 5-10 more mock candidates with varying scores
    ]

def get_mock_company():
    return {
        'name': 'ACME Construction',
        'domain': 'acme.com',
        'admin': 'acme_admin',
        'teams': {
            'Innovation Lab': {'culture': 'collaborative', 'members': ['Nora Ekramy']},
            'Project Alpha': {'culture': 'structured', 'members': ['Ibrahim Khairy']}
        },
        'job_postings': []
    }