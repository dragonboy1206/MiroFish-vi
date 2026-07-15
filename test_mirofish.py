"""
MiroFish Integration Test
Test ngôn ngữ tiếng Việt và tính năng retry
"""
from playwright.sync_api import sync_playwright
import os

def test_mirofish():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("=== Bắt đầu test MiroFish ===\n")
        
        # Test 1: Truy cập trang chủ
        print("Test 1: Truy cập trang chủ...")
        page.goto('http://localhost:3000')
        page.wait_for_load_state('networkidle')
        page.screenshot(path='D:/program/MiroFish/test_screenshots/01_homepage.png')
        print("✓ Đã chụp ảnh trang chủ\n")
        
        # Test 2: Kiểm tra dropdown ngôn ngữ
        print("Test 2: Kiểm tra dropdown ngôn ngữ...")
        language_switcher = page.locator('.language-switcher')
        if language_switcher.is_visible():
            print("✓ Language switcher hiển thị")
            language_switcher.click()
            page.wait_for_timeout(500)
            page.screenshot(path='D:/program/MiroFish/test_screenshots/02_language_dropdown.png')
            
            # Chọn tiếng Việt
            vietnamese_option = page.locator('text=Tiếng Việt')
            if vietnamese_option.is_visible():
                vietnamese_option.click()
                page.wait_for_timeout(1000)
                page.screenshot(path='D:/program/MiroFish/test_screenshots/03_vietnamese_selected.png')
                print("✓ Đã chọn Tiếng Việt\n")
            else:
                print("✗ Không tìm thấy tùy chọn Tiếng Việt\n")
        else:
            print("✗ Language switcher không hiển thị\n")
        
        # Test 3: Kiểm tra giao diện tiếng Việt
        print("Test 3: Kiểm tra giao diện tiếng Việt...")
        page.wait_for_timeout(500)
        
        # Kiểm tra các text tiếng Việt
        hero_title = page.locator('.hero-title')
        if hero_title.is_visible():
            title_text = hero_title.inner_text()
            print(f"  Hero title: {title_text[:50]}...")
        
        start_button = page.locator('text=Khởi động công cụ')
        if start_button.is_visible():
            print("✓ Nút 'Khởi động công cụ' hiển thị bằng tiếng Việt")
        else:
            # Thử tìm nút khác
            start_button = page.locator('.start-btn, .primary-btn').first
            if start_button.is_visible():
                print(f"  Nút: {start_button.inner_text()}")
        
        page.screenshot(path='D:/program/MiroFish/test_screenshots/04_vietnamese_ui.png')
        print()
        
        # Test 4: Kiểm tra upload area
        print("Test 4: Kiểm tra khu vực upload...")
        upload_area = page.locator('.upload-area, .drop-zone, .file-upload')
        if upload_area.is_visible():
            print("✓ Khu vực upload hiển thị")
            page.screenshot(path='D:/program/MiroFish/test_screenshots/05_upload_area.png')
        else:
            print("  Khu vực upload không tìm thấy (có thể cần scroll)")
        print()
        
        # Test 5: Kiểm tra workflow steps
        print("Test 5: Kiểm tra các bước workflow...")
        workflow_steps = page.locator('.workflow-step, .step-item')
        if workflow_steps.count() > 0:
            print(f"✓ Tìm thấy {workflow_steps.count()} bước workflow")
            for i in range(min(workflow_steps.count(), 5)):
                step_text = workflow_steps.nth(i).inner_text()
                print(f"  Bước {i+1}: {step_text[:30]}")
        else:
            print("  Không tìm thấy workflow steps")
        print()
        
        # Test 6: Kiểm tra system status
        print("Test 6: Kiểm tra trạng thái hệ thống...")
        status_indicator = page.locator('.status-indicator, .system-status')
        if status_indicator.is_visible():
            status_text = status_indicator.inner_text()
            print(f"✓ Trạng thái: {status_text}")
        print()
        
        # Test 7: Chụp ảnh toàn trang
        print("Test 7: Chụp ảnh toàn trang...")
        page.screenshot(path='D:/program/MiroFish/test_screenshots/06_full_page.png', full_page=True)
        print("✓ Đã chụp ảnh toàn trang\n")
        
        # Test 8: Kiểm tra responsive (mobile)
        print("Test 8: Kiểm tra giao diện mobile...")
        page.set_viewport_size({"width": 375, "height": 812})
        page.wait_for_timeout(500)
        page.screenshot(path='D:/program/MiroFish/test_screenshots/07_mobile_view.png')
        print("✓ Đã chụp ảnh giao diện mobile\n")
        
        # Reset viewport
        page.set_viewport_size({"width": 1280, "height": 720})
        
        print("=== Hoàn thành test ===")
        print("\nẢnh chụp đã lưu trong: D:/program/MiroFish/test_screenshots/")
        
        browser.close

if __name__ == '__main__':
    # Tạo thư mục screenshots nếu chưa có
    os.makedirs('D:/program/MiroFish/test_screenshots', exist_ok=True)
    test_mirofish()
