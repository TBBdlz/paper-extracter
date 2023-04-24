from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import time
import os

def main() -> None:
	download_path = os.path.join(os.getcwd(), "pdf_data")

	wb = openpyxl.load_workbook('guider.xlsx')
	ws = wb['การพัฒนาการจัดการเรียนรู้']

	#? create directory if not exist
	if not os.path.exists(download_path):
		os.makedirs(download_path)
	download_dir = os.path.expanduser(download_path)

	#? Set download directory to ./pdf_data
	options = webdriver.ChromeOptions()
	prefs = {"download.default_directory": download_dir,
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing.enabled": True}
	options.add_experimental_option("prefs", prefs)

	#? Create driver with the specified options
	driver = webdriver.Chrome(service=Service(
		ChromeDriverManager().install()), options=options)

	try:
		for row in range(7, 305):
			# use os to download pdf file into pdf_data/ folder
			url = ws.cell(row=row, column=3).hyperlink.target
			url = url.replace('view', 'download')
			driver.get(url)
		time.sleep(5)
		driver.quit()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()
