package com.wincom.lib;

import java.util.ArrayList;
import java.util.Collections;

public class ScanSlice implements Comparable<ScanSlice>{
	private double startTime;
	private double endTime;
	private ArrayList<Double> power;
	
	public ScanSlice(double startTime, double endTime, ArrayList<Double> power) {
		this.startTime = startTime;
		this.endTime = endTime;
		this.power = power;
	}
	
	public double getStartTime() {
		return startTime;
	}
	
	public double getEndTime() {
		return endTime;
	}
	
	public ArrayList<Double> getPower() {
		return power;
	}
	
	public boolean containsTime(double checkTime) {
		if(checkTime <= endTime && checkTime >= startTime) {
			return true;
		} else {
			return false;
		}
	}
	
	public int getSampleSize() {
		return power.size();
	}
	
	public double getMaxPower() {
		return Collections.max(power);
	}
	
	public double getMinPower() {
		return Collections.min(power);
	}

	@Override
	public int compareTo(ScanSlice compareToThis) {
		if(startTime == compareToThis.getStartTime()) {
			return 0;
		} else if(startTime < compareToThis.getStartTime()) {
			return -1;
		} else {
			return 1;
		}
	}
}
