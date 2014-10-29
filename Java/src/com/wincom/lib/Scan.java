package com.wincom.lib;

import java.util.ArrayList;
import java.util.Collections;

public class Scan {
	private Band band;
	private ArrayList<ScanSlice> measurements;
	
	public Scan(Band band, ArrayList<ScanSlice> measurements) {
		this.band = band;
		this.measurements = measurements;
	}
	
	public Band getBand() {
		return band;
	}
	
	public ArrayList<ScanSlice> getMeasurements() {
		return measurements;
	}
	
	public int getSampleSize() {
		int samplesTaken = 0;
		
		for(ScanSlice slice : measurements) {
			samplesTaken += slice.getSampleSize();
		}
		
		return samplesTaken;
	}
	
	public double getMinStartTime() {
		double minStartTime = 0;
		
		for(ScanSlice slice : measurements) {
			minStartTime = Math.min(slice.getStartTime(), minStartTime);
		}
		
		return minStartTime;
	}
	
	public double getMaxEndTime() {
		double maxEndTime = 0;
		
		for(ScanSlice slice : measurements) {
			maxEndTime = Math.min(slice.getStartTime(), maxEndTime);
		}
		
		return maxEndTime;
	}
	
	public double getMinPower() {
		double minPower = 0;
		
		for(ScanSlice slice : measurements) {
			minPower = Math.min(slice.getMinPower(), minPower);
		}
		
		return minPower;
	}
	
	public double getMaxPower() {
		double maxPower = 0;
		
		for(ScanSlice slice : measurements) {
			maxPower = Math.max(slice.getMaxPower(), maxPower);
		}
		
		return maxPower;
	}
	
	public void sortScanSlices() {
		Collections.sort(measurements);
	}
	
	public ArrayList<Double> mergeAllPowers() {
		ArrayList<Double> allPowers = new ArrayList<Double>();
		Collections.sort(measurements);
		
		for(ScanSlice slice : measurements) {
			allPowers.addAll(slice.getPower());
		}
		
		return allPowers;
	}
	
	public ScanSlice mergeAllSlices() {
		double startTime = getMinStartTime();
		double endTime = getMaxEndTime();
		ArrayList<Double> allPowers = mergeAllPowers();
		
		return new ScanSlice(startTime, endTime, allPowers);
	}
}
