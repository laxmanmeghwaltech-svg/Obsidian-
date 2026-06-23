#!/usr/bin/env python3
"""Download all playbook files from Google Drive using gdown."""
import os
import subprocess
import json
import time
import sys

GDOWN = os.path.expanduser("~/.local/bin/gdown")
BASE_DIR = "/home/z/my-project/playbooks"

# All files with their Google Drive IDs and local names
MAIN_FOLDER_PDFS = {
    "1VCOxgqaq1zT0kqkTkIMbyzEehk3hRoRk": "AI_Prompt_Playbook.pdf",
    "1aYmlQK-QfMLRDz6y2q3NRnq3jlJnJDqC": "Claude_Code_Marketing_Playbook.pdf",
    "1sCuJxHuGTY7tjfg9wN5GEiJsmBp2U2ja": "Claude_Linkedin_Playbook.pdf",
    "1KnWGu9KqjPdOl_w3_rXHH2vJVn3PnDCx": "Design_in_Claude_Code_Playbook.pdf",
    "1CLqUM3uCZ6WpwMvRZfYxpH0EUW2e3bup": "Executive_Strategy_Playbook.pdf",
    "1M4iS8dZr5gzqkCPY5RGfkhVkOUPjeUPY": "Lead_generation_playbook.pdf",
    "1buSNB9sqG38cg2LeA38Z7mlKkiQkzPji": "LinkedIn_Creator_Bible_Playbook.pdf",
    "18LIypVCsypToUCwxfC6bn1tOSSXjnlFA": "LinkedIn_Million_Playbook_chris_donelly.pdf",
    "1w7a83_uAPR0VyZxp19R7K4RLG2zPfnas": "LinkedIn_Playbook_10K_Followers.pdf",
    "19GhrTeIPC72KabbhzdNdazU0LhqcpCWZ": "MATG_The_Marketers_Guide_to_Google_Gemini_and_NotebookLM.pdf",
    "14eFpCKHw6n-Pfca5O0jUoUxBEEV5w-iz": "NotebookLM-Gems-AI-Playbook.pdf",
    "1grlsThS8KB6OZ4cP78OlTRBKSFEwYS_c": "The_AI_Powered_LinkedIn_Carousel_Playbook.pdf",
    "1CvVQzmCTfewXUynE_lSfeMXn441YnwNf": "The_AI_Toolkit_Playbook.pdf",
    "1LG2feNptV1DhP37ICGn8xHMnHZnA4Owa": "The_Custom_GPT_Masterclass_Playbook.pdf",
    "1MHPc_L7LpliIxdaTxwaTzXeq17NXrfiq": "The_Faceless_YouTube_Channel_Blueprint.pdf",
    "1HxMW9BFHu6JI9iayvEPt7d2eER9t_i2w": "The_Outbound_Acquisition_Playbook.pdf",
    "1OMvdc0HlFKU1uJq2sff4Bie3YyShSBg8": "The_Ultimate_LinkedIn_AI_Playbook.pdf",
    "1WDukRShLT7rLBoVN3Ty53riSx_v6Z5BR": "Ultimate_resource_collection_of_mine.pdf",
    "194-S0piabjaClNUGCgd3-BK19iypicuI": "Ultimate_Guide_Making_Money_with_ChatGPT.pdf",
    "1A6j90jp5fWuQgiOZvBwDKZV1k-HFwo5x": "Vibe_coding_prompts.pdf",
    "15B8XzsaEvxlnkQju9W25TZ_U21-6Y-ur": "Viral_LinkedIn_Post_Template_Library.pdf",
    "192AIBRKy0zEQNvXml0JFN0tcD9Md165p": "ViralX_Instagram_Millionaire_E-Book.pdf",
}

ZIP_FILES = {
    "1JvblnUT1nuy5Lp3c1lnEkgbW27Vm_OXJ": "50_Strategy_Playbooks_Laxman_Meghwal.zip",
    "16loMh3p5oDk8gcoVCAuIXjhUkcHIpjer": "Strategy_Advisor_AI_GPT_Gemini_Config.zip",
}

NINETY_NINE_PLUS = {
    "19Y6CP5_GfBNFN3-honaofWuFPf5tayts": "Playbook_01_AI-Powered_Content_Strategy.pdf",
    "13tCpZuDHEKFe_Yeugra_O0h_5yL17X65": "Playbook_02_LinkedIn_Growth_Mastery.pdf",
    "1C5pWZJ-6ar_yasJhJiXdHHadP0UhKsEo": "Playbook_03_Prompt_Engineering_Mastery.pdf",
    "1Z1P4vT5xinsP1DUqY0vIGO6gBDnEJcaj": "Playbook_04_Claude_Code_for_Professionals.pdf",
    "1YQR-WdHPOSV6aegkPWw0wH-j2Mw6lkPW": "Playbook_05_AI_Agent_Building_Blueprint.pdf",
    "1tBChTurtGktTH7AA0-GDL-_eKolYn5Ha": "Playbook_06_Social_Media_Growth_with_AI.pdf",
    "1_0s3SYXIsx13ecE4voikgzf5Ftv9vqU5": "Playbook_07_AI_Slop_Detection_and_Prevention.pdf",
    "1W-D-RNNiFJcSg9Xm9FU_ufv1KeE3dW_9": "Playbook_08_AI_Tool_Stack_Architecture.pdf",
    "1Br6INuynJDQNufqNSLAdkRzEjIR3ikbE": "Playbook_09_Content_Repurposing_Machine.pdf",
    "10FNsgIE_zvtR2vSnJQthzHE1YyxXkH-k": "Playbook_10_Newsletter_Empire_Building.pdf",
    "1RRXfQVhDdzHkwjVBq_v8R7NlnpNcECXU": "Playbook_11_AI_Video_Production_Playbook.pdf",
    "1bkz0xWv4m3CI_7YjbLsdaV8EprEu53kW": "Playbook_12_SEO_Strategy_in_the_AI_Age.pdf",
    "1qI17cb4iiGJ1Cc4Sn-MntSBnpx6-qqwI": "Playbook_13_Personal_Brand_Authority_System.pdf",
    "1GAQFsDq3sAkXwCckRX6xlLER-xnsep4t": "Playbook_14_AI_Marketing_Automation.pdf",
    "1patfpCdEfVfVrCNADJ2PqgnCy3PHX9Gp": "Playbook_15_Creative_Direction_with_AI.pdf",
    "1tw0SMaM1KnELAP8lLFbPcgohK6Pp4k4y": "Playbook_16_AI_Copywriting_Playbook.pdf",
    "14XIcJnuKOJt-lO8VjxPGbPjMLkIwlFfz": "Playbook_17_Business_Strategy_with_AI.pdf",
    "1Kc_LtGe_4eBhGRxheaUn1-eMaL8THqLd": "Playbook_18_AI_Sales_Enablement.pdf",
    "1PJTG_fRjIeoVzLRWZ3j5YZwoFlrzVzrB": "Playbook_19_Data-Driven_Decision_Making.pdf",
    "1fCu-8ni9ZX0IwWWkFtUUBp3M9hhsezim": "Playbook_20_AI_Productivity_Systems.pdf",
    "1zp_gJxul1U49azfKXtw8Ve7O9itHT-Wb": "Playbook_21_Influencer_Marketing_with_AI.pdf",
    "1IG3vnxijDBYYWzOK5J1XCzx4x7BusJB0": "Playbook_22_AI_Second_Brain_Building.pdf",
    "10NglD0lv1PXTmXZCpzPM_qzpCGQP3I3e": "Playbook_23_Revenue_Growth_Framework.pdf",
    "1VeTovvIziIpw-2f0BFXUQYL-O5_K-lWk": "Playbook_24_Customer_Journey_Optimization.pdf",
    "1JfWwGBvDmiJG7vk7o8h7a1y0zNPIE_fV": "Playbook_25_AI_Product_Launch_Strategy.pdf",
    "1voKJQr5i4veIol0NYStsgByKAznPCg7M": "Playbook_26_Thought_Leadership_Accelerator.pdf",
    "1sCY9-_Pz6cNu2jhzmFhgtbS_nOIarPo7": "Playbook_27_AI_Workflow_Design_Patterns.pdf",
    "1o1qPCfWgd0QK5_TNqMZ7hlfgKhCmEce6": "Playbook_28_Digital_Advertising_with_AI.pdf",
    "1v0kRmz4ajFNT1H2-_hSbkcv25J6iDDWv": "Playbook_29_Community_Building_Playbook.pdf",
    "1jlvmk8oWU6ThK-_jvEkyJhPd3n8Ob5v0": "Playbook_30_AI_Consulting_Framework.pdf",
    "1YtUmyVqT5MOBMjkHEcC6HzxEeyfNfp9F": "Playbook_31_Email_Marketing_Intelligence.pdf",
    "1pAFYJGLvLGBJCYVDdrArFC4Cl8E8Ehqj": "Playbook_32_Competitive_Intelligence_with_AI.pdf",
    "1jEvjDFr8VTjP1fO7GnlPYHTKXeM7sZvN": "Playbook_33_AI-Powered_Freelancing.pdf",
    "1rlk2AU56NeksmqSNQyIoorMbLtYrDApd": "Playbook_34_B2B_Marketing_Transformation.pdf",
    "1gEz48ji_hwicYt5T7uVVI60P6QubewT1": "Playbook_35_AI_Ethics_and_Governance.pdf",
    "1OHFiR5Zd1nyKvKAcUj9kwQr1LmgWEYDC": "Playbook_36_Startup_Growth_with_AI.pdf",
    "15PofTDQFQ-G8kKFVeHJ5VhP8Xgc885rH": "Playbook_37_AI_Customer_Experience.pdf",
    "1EYvVKBqqWrJD1l7PBLFt6aoXrvm35rIw": "Playbook_38_Brand_Building_in_the_AI_Era.pdf",
    "1cnte80oAZrfTfRWhIkQ7qrNz3N3sNz8J": "Playbook_39_AI_Research_and_Analysis.pdf",
    "1a4aDBwVe0fsIgu4q9Fj3C1jGCrXlG-E1": "Playbook_40_Podcast_Growth_with_AI.pdf",
    "1ATqK0pyHHN7IVtEJJOwMWdCm-MKHc5w0": "Playbook_41_AI_Talent_and_Hiring.pdf",
    "1PF4xLn1LIBrAhidtug9xIC-ZvK0ce1-c": "Playbook_42_Conversion_Rate_Optimization.pdf",
    "1mHLllrUnYCc9PcRdoAVOPwXwrmqjjpvi": "Playbook_43_AI_Operations_Playbook.pdf",
    "1sfwRsXsDC8-w0y5E2H05LPILVi6aEmdp": "Playbook_44_Public_Speaking_and_AI.pdf",
    "1qOyU8g7GRPZJRvEUoKYXn-JxSlqiAPRY": "Playbook_45_AI_Financial_Strategy.pdf",
    "1GTURrLPQIejttJxqqWHFCwp5N55QKTNd": "Playbook_46_Remote_Team_AI_Integration.pdf",
    "1n61ctKCMcpkaanmLgcxcuHdQjcCvUbHR": "Playbook_47_AI_Innovation_Framework.pdf",
    "1CBuRhY16irArEndMdOGp2KRu-yY3rSHQ": "Playbook_48_Digital_Transformation_Playbook.pdf",
    "1Me82PbdDmFody2Kmz2KskdsrM3QLYsdj": "Playbook_49_AI_Risk_Management.pdf",
}

GPT_INSTRUCTIONS = {
    "10jlQs_Jt0PMhKNdBvJz4mSqhhIYnWISt": "Knowledge_Bundle_AI_Tools_and_Prompt_Engineering.pdf",
    "1CcHzZnMIKWRZzgHkC_XtswT79iu2o9nK": "Knowledge_Bundle_Business_Strategy_and_Intelligence.pdf",
    "1qRt1W2B4JKZMTs5OwxijOjhyiiGjNiIJ": "Knowledge_Bundle_Content_and_Marketing_AI.pdf",
    "1qaRo1lPCwgQ2PmSulHiay6FwRh1TBjC7": "Knowledge_Bundle_Customer_and_Brand.pdf",
    "1vTjLeoRMOBVYrCnRR2N7pgdsG_7ptvQI": "Knowledge_Bundle_Ethics_Risk_and_Governance.pdf",
    "1vgdcRXJC0cDLFPj-JMQxAxFtjmJPlsGx": "Knowledge_Bundle_Operations_and_Productivity.pdf",
    "1_nNV2XwWdKYPci4BYsMZ8dugndY72FbA": "Knowledge_Bundle_Personal_Brand_and_Thought_Leadership.pdf",
    "1xtliEgl4qyGprLFwKQyCLagLpTmBCL03": "Knowledge_Bundle_Revenue_and_Sales.pdf",
    "1Z_igi3MzRAXz8DRc23EIuPB-jDvc_HO6": "Knowledge_Bundle_SEO_Email_and_Newsletter.pdf",
    "1wBFif_mp4mEvy_lei92BeoF8W6hEb8Qu": "Knowledge_Bundle_Startup_and_Innovation.pdf",
    "15J4_nQqB2is3oxvDpfSsptQRwO_V2xbE": "Setup_Guide_GPT_and_Gemini_Gem.pdf",
    "1PgPlLS1gDp9vQmmyKd6JTSRCbiJVqUn8": "Gemini_Gem_Configuration.json",
    "1hOmxpU3QMoU0t5np2e_OJGTKWMVM6Hot": "GPT_Configuration.json",
    "1K1oAmgnInDcTqHCU4xBSc7ZW3slFaETl": "System_Prompt_Strategy_Advisor_AI.md",
}

def download_file(file_id, output_path, max_retries=3):
    """Download a single file from Google Drive using gdown."""
    for attempt in range(max_retries):
        try:
            url = f"https://drive.google.com/uc?id={file_id}"
            result = subprocess.run(
                [GDOWN, url, "-O", output_path, "--no-cookies"],
                capture_output=True, text=True, timeout=300
            )
            if result.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                print(f"  OK: {os.path.basename(output_path)} ({os.path.getsize(output_path)} bytes)")
                return True
            else:
                print(f"  Retry {attempt+1}: {os.path.basename(output_path)} - {result.stderr[:100]}")
        except subprocess.TimeoutExpired:
            print(f"  Timeout {attempt+1}: {os.path.basename(output_path)}")
        except Exception as e:
            print(f"  Error {attempt+1}: {os.path.basename(output_path)} - {str(e)[:100]}")
        time.sleep(2)
    return False

def download_batch(files_dict, output_dir):
    """Download a batch of files."""
    os.makedirs(output_dir, exist_ok=True)
    success = 0
    failed = []
    for file_id, filename in files_dict.items():
        output_path = os.path.join(output_dir, filename)
        if os.path.exists(output_path) and os.path.getsize(output_path) > 100:
            print(f"  SKIP (exists): {filename}")
            success += 1
            continue
        if download_file(file_id, output_path):
            success += 1
        else:
            failed.append(filename)
    return success, failed

if __name__ == "__main__":
    print("=" * 60)
    print("DOWNLOADING ALL PLAYBOOK FILES FROM GOOGLE DRIVE")
    print("=" * 60)
    
    total_success = 0
    total_failed = []
    
    # 1. Download main folder PDFs
    print("\n[1/4] Downloading main folder PDFs...")
    s, f = download_batch(MAIN_FOLDER_PDFS, f"{BASE_DIR}/main_pdfs")
    total_success += s
    total_failed.extend(f)
    
    # 2. Download ZIP files
    print("\n[2/4] Downloading ZIP files...")
    s, f = download_batch(ZIP_FILES, f"{BASE_DIR}/zips")
    total_success += s
    total_failed.extend(f)
    
    # 3. Download 99+ systems playbooks
    print("\n[3/4] Downloading 99+ systems playbooks...")
    s, f = download_batch(NINETY_NINE_PLUS, f"{BASE_DIR}/99plus_systems")
    total_success += s
    total_failed.extend(f)
    
    # 4. Download GPT instruction files
    print("\n[4/4] Downloading GPT instruction files...")
    s, f = download_batch(GPT_INSTRUCTIONS, f"{BASE_DIR}/gpt_instructions")
    total_success += s
    total_failed.extend(f)
    
    print("\n" + "=" * 60)
    print(f"DOWNLOAD COMPLETE: {total_success} succeeded, {len(total_failed)} failed")
    if total_failed:
        print(f"Failed files: {total_failed}")
    print("=" * 60)
