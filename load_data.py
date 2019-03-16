class CourseData:

    def __init__(self, filename):

        import json
        from pprint import pprint

        with open(filename, encoding="utf8") as f:
            self.data = json.load(f)["items"] 
            # data is a list of dictionaries, each corresponding to a course

    def get_course_count(self):
        """Returns: int, total number of courses"""

        course_count = 0
        for entry in self.data:
            if entry["type"] == "Class":
                course_count += 1
        return course_count

    def get_full_list(self):
        """Returns: list, copy of full list generated by json file"""

        return self.data.copy()

    def get_course_list(self):
        """Returns: list, list of all classes available (id)"""

        ans = []
        for entry in self.data:
            if entry["type"] == "Class":
                ans.append(entry["id"])
        return ans

    def create_course_dict(self):
        """Returns: dictionary of dictionaries, the first dictionary is keyed by a string
        of the class id, the second has the following keys.
        'type': with possibilities 'Class', 'RecitationSession', 'LectureSession', 'LabSession'
        'label': course title
        'level':
        'description'
        'prereqs'
        'equivalent_subjects'
        'joint_subjects'
        'hass_attribute'
        'gir_attribute'
        'total-units'
        'course'
        """
        course_dict = {}

        for entry in self.data:
            if entry["type"] == "Class":
                
                entry_dict = {}

                entry_dict["label"] = entry["label"] 
                entry_dict["level"] = entry["level"]
                entry_dict["description"] = entry["description"]
                entry_dict["prereqs"] = entry["prereqs"]
                entry_dict["equivalent_subjects"] = entry["equivalent_subjects"]
                entry_dict["joint_subjects"] = entry["joint_subjects"]
                entry_dict["hass_attribute"] = entry["hass_attribute"]
                entry_dict["gir_attribute"] = entry["gir_attribute"]
                entry_dict["total-units"] = entry["total-units"]
                entry_dict["course"] = entry["course"]

                course_dict[entry["id"]] = entry_dict
                
        return course_dict

    def print_courses(self):
        """Prints list of courses, as well as their descriptions, procedurally.
        Returns: None"""

        import time

        course_count = 0
        for entry in self.data:
            if entry["type"] == "Class":
                print(entry["id"] + ": " + entry["label"])
                time.sleep(0.001)

        print("Length: " + str(self.get_course_count()))

        
data = CourseData("course_data.json")
print(data.print_courses())

