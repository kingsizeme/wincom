package com.wincom.lib;

public class Band {
	private double startFrequency;
	private double endFrequency;
	private String description;
	
	public Band(double startFrequency, double endFrequency, String description) {
		this.startFrequency = startFrequency;
		this.endFrequency = endFrequency;
		this.description = description;
	}
	
	public String getDescription() {
		return description;
	}
	
	public double getStartFrequency() {
		return startFrequency;
	}
	
	public double getEndFrequency() {
		return endFrequency;
	}

	public double getBandwidth() {
		return endFrequency - startFrequency;
	}
	
	public boolean containsFrequency(double checkFrequency) {
		if(checkFrequency <= endFrequency && checkFrequency >= startFrequency) {
			return true;
		} else {
			return false;
		}
	}
	
	public String toString() {
		String stringRepresentation = "Desc: " + description + 
				" Start Freq: " + startFrequency + 
				" End Freq: " + endFrequency;
		
		return stringRepresentation;
	}
}
