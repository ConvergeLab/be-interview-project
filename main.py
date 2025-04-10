from trace_extractor import PCBTraceExtractor


if __name__ == "__main__":
    extractor = PCBTraceExtractor()
    extractor.load_json_file("Vacuum_PCB_OBjects.json")
    # test casses

    # print(extractor.extract_trace_between_pads(pad1, pad2))
    # pad1 = extractor.desgignator2_pad_number2_pad["C41"]["1"]
    # pad2 = extractor.desgignator2_pad_number2_pad["C3"]["1"]
    # print(extractor.extract_trace_between_pads(pad1, pad2))



    assert abs(
        extractor.extract_traces_between_pads("U1", "11", "R66", "1") - 5.30688
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "61", "C43", "2") - 5.90118
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "20", "C3", "2") - 2.09999
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "20", "R2", "1") - 3.73421
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "9", "D5", "2") - 9.97167
    ) < 0.1



    assert abs(
        extractor.extract_traces_between_pads("R35", "2", "Q6", "4") - 2.07941
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R32", "2", "Q6", "4") - 4.96667
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "22", "R17", "1") - 10.15418
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "15", "C2", "1") - 5.95187
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "19", "R15", "1") - 9.65903
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "47", "C38", "2") - 38.54960
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "6", "C26", "1") - 4.84104
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "66", "C28", "2") - 29.57893
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R85", "1", "U1", "65") - 36.95201
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R73", "2", "C31", "2") - 48.54113
    ) < 0.1
