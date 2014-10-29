package com.wincom.parser;

import java.io.File;
import java.util.ArrayList;

import com.wincom.lib.Band;
import com.wincom.lib.Scan;

public interface FileParser {
	
	public File open_file(String filePath);
	
	public ArrayList<Band> getBands(File inputFile);
	
	public ArrayList<Scan> getData(File inputFile);
	
	public ArrayList<Scan> getDataForBand(File inputFile, int bandIndex);
}
