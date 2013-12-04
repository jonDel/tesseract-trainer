 pdftoppm -tiff -r 300 claub_pdf.pdf claub
 mv claub-1.tif por.test_font.exp0
 tesseract  por.test_font.exp0.tif por.test_font.exp0 batch.nochop makebox
 ## Corrigir box file com o editor de boxes jtessbox editor
 tesseract -l por por.test_font.exp0.tif por.test_font.exp0 nobatch box.train
 unicharset_extractor por.test_font.exp0.box
 echo "test_font 1 0 0 0 0" > font_properties
 shapeclustering -F font_properties -U unicharset por.test_font.exp0.tr 
 unicharset_extractor por.test_font.exp0.box
 shapeclustering -F font_properties -U unicharset por.test_font.exp0.tr 
 mftraining -F font_properties -U unicharset -O por.unicharset por.test_font.exp0.tr
 cntraining por.test_font.exp0.tr
 mv inttemp por.inttemp 
 mv normproto por.normproto 
 mv pffmtable por.pffmtable 
 mv shapetable por.shapetable 
 combine_tessdata por.
 sudo cp /usr/share/tesseract-ocr/tessdata/por.traineddata /usr/share/tesseract-ocr/tessdata/por.traineddata_old 
 sudo cp por.traineddata /usr/share/tesseract-ocr/tessdata/
 tesseract claub-2.tif testocr -l por
 vi testocr.txt
