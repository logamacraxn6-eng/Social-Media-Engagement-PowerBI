# Social Media Engagement Analytics Dashboard
## Overview
Interactive Power BI analysis of social-media content performance across Instagram, YouTube, Facebook and LinkedIn.

**Dataset:** 1,200 synthetic posts covering January–December 2025. Created for learning/portfolio use; it contains no real users or private platform data.

## Objectives
- Track social-media KPIs
- Compare platform performance
- Evaluate content types/categories
- Analyze engagement trends
- Identify posting-time patterns
- Produce content-strategy recommendations

## Tools
Python, Pandas, Microsoft Power BI, DAX

## Structure
```text
Social_Media_Engagement_PowerBI_Project/
├── data/social_media_engagement.csv
├── notebooks/social_media_analysis.ipynb
├── powerbi/DAX_Measures.md
├── powerbi/POWER_BI_BUILD_GUIDE.md
├── reports/project_report.txt
├── reports/linkedin_caption.txt
└── README.md
```

## Dashboard
**Page 1:** Social Media Overview  
**Page 2:** Content Performance  
**Page 3:** Best Posting Time

## Analysis
Average engagement rate by platform:
Platform
YouTube      8.417482
Instagram    8.404547
LinkedIn     7.926703
Facebook     7.370044

Average engagement rate by content type:
Content_Type
Short       9.199144
Video       8.500586
Image       7.855193
Carousel    7.489772
Text        7.272533

Average engagement rate by time slot:
Time_Slot
Afternoon    8.541212
Evening      8.120346
Morning      7.945031
Night        7.855398

These are synthetic results and should not be presented as real-world benchmarks.

## How to Use
1. Open Power BI Desktop.
2. Import `data/social_media_engagement.csv`.
3. Rename the table to `SocialMedia`.
4. Add measures from `powerbi/DAX_Measures.md`.
5. Follow `POWER_BI_BUILD_GUIDE.md`.
6. Save as `Social_Media_Engagement_Dashboard.pbix`.

## Responsible Use
Real social-media data should be obtained through authorized APIs or platform exports and handled according to platform terms and privacy requirements.
